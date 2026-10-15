"""Automated checks for saving, editing, completion, and safe HTTP methods."""
from datetime import date, timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .forms import TaskForm
from .models import Task, next_occurrence

class TaskTests(TestCase):
    def setUp(self):
        self.today = timezone.localdate()
        self.task = Task.objects.create(title="Water plants", frequency="weekly", next_due_date=self.today)

    def test_dashboard_shows_saved_task(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Water plants")

    def test_create_and_edit_task(self):
        response = self.client.post(reverse("task_add"), {"title": "Read", "description": "10 pages", "frequency": "daily", "next_due_date": str(self.today)})
        self.assertRedirects(response, reverse("dashboard"))
        task = Task.objects.get(title="Read")
        self.client.post(reverse("task_edit", args=[task.pk]), {"title": "Read book", "description": "", "frequency": "once", "next_due_date": str(self.today)})
        task.refresh_from_db()
        self.assertEqual(task.title, "Read book")

    def test_blank_title_rejected(self):
        form = TaskForm(data={"title": "  ", "frequency": "once", "next_due_date": str(self.today)})
        self.assertFalse(form.is_valid())

    def test_repeating_task_moves_forward(self):
        self.client.post(reverse("task_complete", args=[self.task.pk]))
        self.task.refresh_from_db()
        self.assertEqual(self.task.next_due_date, self.today + timedelta(days=7))
        self.assertFalse(self.task.is_completed)
        self.assertIsNotNone(self.task.last_completed_at)

    def test_one_time_task_stays_completed(self):
        self.task.frequency = "once"
        self.task.save()
        self.client.post(reverse("task_complete", args=[self.task.pk]))
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)

    def test_changes_require_post(self):
        for name in ("task_complete", "task_delete"):
            self.assertEqual(self.client.get(reverse(name, args=[self.task.pk])).status_code, 405)
        self.assertTrue(Task.objects.filter(pk=self.task.pk).exists())

    def test_delete_task(self):
        self.client.post(reverse("task_delete", args=[self.task.pk]))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_month_end_is_safe(self):
        # A monthly task due on the 31st must not crash in shorter months.
        result = next_occurrence(date(2024, 1, 31), "monthly")
        self.assertGreater(result, self.today)
        self.assertLessEqual(result.day, 31)

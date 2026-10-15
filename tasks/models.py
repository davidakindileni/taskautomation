"""Database structure and the logic for repeating a task."""
import calendar
from datetime import timedelta
from django.db import models
from django.utils import timezone


def next_occurrence(due_date, frequency):
    """Return the next scheduled date strictly after today.

    Advancing from the previous due date (rather than today's date) keeps
    a weekly task on its original weekday. Missed dates are skipped.
    """
    today = timezone.localdate()
    current = due_date
    if frequency == "daily":
        return max(current + timedelta(days=1), today + timedelta(days=1))
    if frequency == "weekly":
        steps = max(1, ((today - current).days // 7) + 1)
        return current + timedelta(weeks=steps)
    if frequency == "monthly":
        # Keep the original day where possible; clamp e.g. January 31 to February 28.
        original_day = due_date.day
        while True:
            month = current.month + 1
            year = current.year + (month > 12)
            month = 1 if month > 12 else month
            day = min(original_day, calendar.monthrange(year, month)[1])
            current = current.replace(year=year, month=month, day=day)
            if current > today:
                return current
    raise ValueError("Unknown frequency")


class Task(models.Model):
    FREQUENCIES = [("once", "One time"), ("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly")]
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCIES, default="once")
    next_due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    last_completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["is_completed", "next_due_date", "title"]

    def __str__(self):
        return self.title

    def complete(self):
        """Finish a one-time task, or reschedule a repeating task."""
        if self.is_completed:
            return
        self.last_completed_at = timezone.now()
        if self.frequency == "once":
            self.is_completed = True
        else:
            self.next_due_date = next_occurrence(self.next_due_date, self.frequency)
        self.save()

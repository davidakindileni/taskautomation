"""Each view receives a browser request and returns a dynamic HTML page."""
from datetime import timedelta
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST
from .forms import TaskForm
from .models import Task, TaskCompletion


def dashboard(request):
    """Separate tasks by status so the dashboard is easy to understand."""
    today = timezone.localdate()
    tasks = Task.objects.all()
    return render(request, "tasks/dashboard.html", {
        "upcoming": tasks.filter(is_completed=False, next_due_date__gte=today).order_by("next_due_date"),
        "overdue": tasks.filter(is_completed=False, next_due_date__lt=today).order_by("next_due_date"),
        "completed": tasks.filter(is_completed=True).order_by("-last_completed_at"),
        "history": TaskCompletion.objects.select_related("task").all(),
        "due_soon_limit": today + timedelta(days=7),
        "today": today,
        "total": tasks.count(),
    })


def task_form(request, pk=None):
    """One page handles both adding and editing a task."""
    task = get_object_or_404(Task, pk=pk) if pk is not None else None
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Task saved successfully.")
        return redirect("dashboard")
    return render(request, "tasks/task_form.html", {"form": form, "task": task})


@require_POST
def complete_task(request, pk):
    """Only POST requests can change a task's completion state."""
    task = get_object_or_404(Task, pk=pk)
    if task.complete():
        if task.is_completed:
            messages.success(request, "Task completed and added to completion history.")
        else:
            messages.success(request, "Completion recorded. Your recurring task has been rescheduled.")
    else:
        messages.info(request, "This task was already completed.")
    return redirect("dashboard")


@require_POST
def delete_task(request, pk):
    """Delete the selected task after browser confirmation."""
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.success(request, "Task deleted.")
    return redirect("dashboard")

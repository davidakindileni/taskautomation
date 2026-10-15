"""Optional Django admin interface for viewing task records."""
from django.contrib import admin
from .models import Task, TaskCompletion

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "frequency", "next_due_date", "is_completed")
    list_filter = ("frequency", "is_completed")
    search_fields = ("title",)


@admin.register(TaskCompletion)
class TaskCompletionAdmin(admin.ModelAdmin):
    """View completed occurrences separately from active recurring tasks."""
    list_display = ("task_title", "scheduled_due_date", "completed_at")
    list_filter = ("completed_at",)
    search_fields = ("task_title",)

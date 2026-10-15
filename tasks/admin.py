"""Optional Django admin interface for viewing task records."""
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "frequency", "next_due_date", "is_completed")
    list_filter = ("frequency", "is_completed")
    search_fields = ("title",)

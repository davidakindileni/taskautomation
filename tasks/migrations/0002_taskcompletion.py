# Add a history table without changing or deleting existing tasks.
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [("tasks", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="TaskCompletion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("task_title", models.CharField(max_length=120)),
                ("scheduled_due_date", models.DateField()),
                ("completed_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("task", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="completions", to="tasks.task")),
            ],
            options={"ordering": ["-completed_at", "-pk"]},
        ),
    ]

# Initial database migration. Django uses this file to create the tasks table.
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
                ("frequency", models.CharField(choices=[("once", "One time"), ("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly")], default="once", max_length=10)),
                ("next_due_date", models.DateField()),
                ("is_completed", models.BooleanField(default=False)),
                ("last_completed_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["is_completed", "next_due_date", "title"]},
        ),
    ]

# Task Automation Web App

**Course:** CSE 310 – Applied Programming | **Module:** 3 – Web Apps

## Overview
A simple Django web application for managing one-time and recurring tasks. It uses SQLite, dynamic HTML pages, and validated forms. The dashboard displays overdue, upcoming, due-soon (within 7 days), and completed one-time tasks.

## Quick start (Windows PowerShell)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000/ in your browser. See `INSTALLATION_GUIDE.pdf` for detailed setup, troubleshooting, and test instructions.

## Main pages and interactions
- `/` displays saved tasks from SQLite.
- `/tasks/new/` creates a task with a validated form.
- `/tasks/<id>/edit/` edits an existing task.
- POST-only complete and delete actions change saved records.
- For repeating tasks, **Complete** records the completion and advances the due date; the task remains active. For one-time tasks, it moves to Completed.

## Tools and technologies
Python 3.12, Django 5.2, HTML, CSS, SQLite, and a web browser. No external services or JavaScript packages are required.

## Testing
Run `python manage.py test` after installing requirements and migrating. Manually create, edit, complete, and delete tasks in the browser. The included tests cover key workflows.

## Important limitations
This is a **single-user local classroom demonstration**, not a hosted production service. There is no login, notification system, or background scheduler. "Automation" means a repeating task automatically receives its next due date **when the user clicks Complete**; it does not run jobs by itself. The database file is created by `migrate` and is intentionally excluded from the ZIP.

## Demo video
YouTube URL: 

## Helpful references
- Django tutorial: https://docs.djangoproject.com/en/5.2/intro/tutorial01/
- Django forms: https://docs.djangoproject.com/en/5.2/topics/forms/
- Django models: https://docs.djangoproject.com/en/5.2/topics/db/models/
- Django testing: https://docs.djangoproject.com/en/5.2/topics/testing/
- Python virtual environments: https://docs.python.org/3/library/venv.html
- SQLite: https://www.sqlite.org/docs.html

## Future work
Add user accounts, reminders, a completion history, and background scheduling.

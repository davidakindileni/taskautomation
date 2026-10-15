# Task Automation Web App

**Course:** CSE 310 – Applied Programming | **Module:** 3 – Web Apps

## Overview
A simple Django web application for managing one-time and recurring tasks. It uses SQLite, dynamic HTML pages, and validated forms. The dashboard displays overdue, upcoming, due-soon (within 7 days), and completed one-time tasks, plus a separate completion history for all finished occurrences.

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
- For repeating tasks, **Complete** creates a completion-history record and advances the due date; the task remains active for its next occurrence. For one-time tasks, it moves to Finished One-Time Tasks and also appears in Completion History.

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
Add user accounts, reminders, history filtering/export, and background scheduling.

## Updating an existing installation
If you already have a `db.sqlite3` database, **back it up** before replacing files.
Replace the project code, keep your existing database, then run:

```powershell
python manage.py migrate
python manage.py test
python manage.py runserver
```

The `0002_taskcompletion` migration adds a new table and preserves existing tasks.
Old completions cannot be reconstructed reliably, so history begins with completions
made after this update. Deleting a task also deletes its completion history.

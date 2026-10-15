#!/usr/bin/env python
"""Django's command-line entry point (runserver, migrate, test, etc.)."""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_automation.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

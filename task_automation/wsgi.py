"""WSGI entry point, included for standard Django compatibility."""
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_automation.settings")
application = get_wsgi_application()

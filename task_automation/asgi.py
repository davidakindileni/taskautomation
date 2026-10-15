"""ASGI entry point, included for standard Django compatibility."""
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_automation.settings")
application = get_asgi_application()

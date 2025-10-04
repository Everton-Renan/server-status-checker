import os

from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig


class MonitorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "monitor"

    def ready(self) -> None:
        if os.environ.get("RUN_MAIN", None) != "true":
            return

        from .models import Settings
        from .tasks import create_log

        check_interval = Settings.objects.first()

        scheduler = BackgroundScheduler()

        if check_interval is None:
            scheduler.add_job(create_log, "interval", seconds=300)
        else:
            scheduler.add_job(
                create_log, "interval", seconds=check_interval.check_interval_seconds
            )
        scheduler.start()

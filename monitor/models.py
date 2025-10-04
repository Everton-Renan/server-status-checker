from django.db import models


# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class CheckLog(models.Model):
    class Meta:
        verbose_name_plural = "Check Logs"

    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    status_code = models.IntegerField()
    response_time = models.FloatField()
    error = models.CharField(default="")
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.server.name


class Settings(models.Model):
    class Meta:
        verbose_name_plural = "Settings"

    check_interval_seconds = models.PositiveIntegerField(
        default=300,
        help_text="It will be necessary to restart the application for the new interval to take effect.",
    )

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

    server = models.ForeignKey(Server, on_delete=models.CASCADE, editable=False)
    status_code = models.IntegerField(editable=False)
    response_time = models.FloatField(editable=False)
    checked_at = models.DateTimeField(auto_now_add=True, editable=False)

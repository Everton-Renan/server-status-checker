import requests

from .models import CheckLog, Server


def create_log():
    servers = Server.objects.all()
    if servers is not None:
        for server in servers:
            if server.is_active is False:
                continue

            e = None
            try:
                request = requests.get(url=server.url)
            except requests.exceptions.RequestException as error:
                e = error

            if e is not None:
                log = CheckLog.objects.create(
                    server=server,
                    status_code=0,
                    error=str(e),
                    response_time=0,
                )
                log.save()
            else:
                log = CheckLog.objects.create(
                    server=server,
                    status_code=request.status_code,
                    response_time=request.elapsed.total_seconds(),
                )
                log.save()

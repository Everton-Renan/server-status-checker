from django.contrib import admin

from .models import CheckLog, Server


# Register your models here.
@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url", "is_active")
    list_display_links = ("id", "name", "url", "is_active")
    search_fields = ("id", "name", "url")


@admin.register(CheckLog)
class CheckLogAdmin(admin.ModelAdmin):
    list_display = ("id", "server", "status_code", "response_time", "checked_at")
    list_display_links = ("id", "server", "status_code", "response_time", "checked_at")
    search_fields = ("id", "server")

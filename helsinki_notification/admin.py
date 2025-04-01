from django.contrib import admin
from django.utils.translation import get_language
from django.utils.translation import gettext as _

from helsinki_notification.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_filter = ["type"]
    search_fields = [
        "title_fi",
        "content_fi",
        "title_sv",
        "content_sv",
        "title_en",
        "content_en",
    ]
    readonly_fields = ["created_at", "modified_at"]
    fieldsets = [
        (
            _("Notification details"),
            {
                "fields": [
                    "title_fi",
                    "content_fi",
                    "title_sv",
                    "content_sv",
                    "title_en",
                    "content_en",
                    "type",
                ]
            },
        ),
        (
            _("External URL"),
            {
                "fields": [
                    "external_url_title_fi",
                    "external_url_fi",
                    "external_url_title_sv",
                    "external_url_sv",
                    "external_url_title_en",
                    "external_url_en",
                ]
            },
        ),
        (
            _("Validity period"),
            {"fields": ["validity_period_start", "validity_period_end"]},
        ),
        (
            _("System fields"),
            {
                "fields": [
                    "created_at",
                    "modified_at",
                ]
            },
        ),
    ]

    def get_list_display(self, *_):
        list_display = ["type", "validity_period_start", "validity_period_end"]

        # Add a locale-appropriate title.
        lang = get_language()
        if lang.startswith("fi"):
            list_display = ["title_fi", *list_display]
        elif lang.startswith("sv"):
            list_display = ["title_sv", *list_display]
        else:
            list_display = ["title_en", *list_display]

        return list_display

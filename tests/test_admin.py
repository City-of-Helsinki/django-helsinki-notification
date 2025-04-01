import pytest
from django.contrib.admin import AdminSite
from django.utils import translation

from helsinki_notification.admin import NotificationAdmin
from helsinki_notification.models import Notification


@pytest.mark.parametrize(
    "lang,expected",
    [("fi", "title_fi"), ("sv", "title_sv"), ("en", "title_en"), ("fr", "title_en")],
)
def test_get_list_display(lang, expected):
    model_admin = NotificationAdmin(Notification, AdminSite())
    with translation.override(lang):
        assert model_admin.get_list_display() == [
            expected,
            "type",
            "validity_period_start",
            "validity_period_end",
        ]

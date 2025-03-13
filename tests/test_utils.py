import pytest

from helsinki_notification.utils import map_translated_field


def test_map_translated_field_returns_dict_of_translations(notification_factory):
    notification = notification_factory.build()
    assert map_translated_field(notification, "title") == {
        "fi": notification.title_fi,
        "sv": notification.title_sv,
        "en": notification.title_en,
    }


def test_map_translated_field_raises_error_on_missing_field(notification_factory):
    notification = notification_factory.build()
    with pytest.raises(AttributeError):
        map_translated_field(notification, "banana hammock")

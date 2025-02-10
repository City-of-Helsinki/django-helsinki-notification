import pytest
from freezegun import freeze_time

from pulu.models import Notification
from pulu_tests.utils import values_list, values_list_from_dict


@freeze_time("2025-01-01T12:00:00Z")
@pytest.mark.django_db
def test_rest_framework_list_endpoint(
    notification_factory, valid_notification_factory, relative_now, client
):
    # Past notification
    notification_factory(
        validity_period_start=relative_now.yesterday,
        validity_period_end=relative_now.last_second,
    )
    # Future notification
    notification_factory(
        validity_period_start=relative_now.next_hour,
        validity_period_end=relative_now.far_future,
    )
    expected_order = [
        valid_notification_factory(type=Notification.Type.ERROR),
        valid_notification_factory(type=Notification.Type.ALERT),
        valid_notification_factory(type=Notification.Type.INFO),
    ]

    response = client.get("/drf/notifications")

    assert response.status_code == 200
    assert len(response.data) == len(expected_order)
    assert values_list_from_dict(response.data, "id") == values_list(
        expected_order, "id"
    )

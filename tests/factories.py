from datetime import timedelta

import factory
from django.utils import timezone
from pytest_factoryboy import register

from helsinki_notification.models import Notification


@register
class NotificationFactory(factory.django.DjangoModelFactory):
    title_fi = factory.Faker("sentence", locale="fi_FI")
    title_sv = factory.Faker("sentence", locale="sv_SE")
    title_en = factory.Faker("sentence", locale="en_US")

    external_url_fi = factory.Faker("url", locale="fi_FI")
    external_url_sv = factory.Faker("url", locale="sv_SE")
    external_url_en = factory.Faker("url", locale="en_US")

    external_url_title_fi = factory.Faker("sentence", locale="fi_FI")
    external_url_title_sv = factory.Faker("sentence", locale="sv_SE")
    external_url_title_en = factory.Faker("sentence", locale="en_US")

    content_fi = factory.Faker("text", locale="fi_FI")
    content_sv = factory.Faker("text", locale="sv_SE")
    content_en = factory.Faker("text", locale="en_US")

    class Meta:
        model = Notification


@register
class ValidNotificationFactory(NotificationFactory):
    validity_period_start = factory.LazyAttribute(lambda _: timezone.now())
    validity_period_end = factory.LazyAttribute(
        lambda o: o.validity_period_start + timedelta(days=999)
    )

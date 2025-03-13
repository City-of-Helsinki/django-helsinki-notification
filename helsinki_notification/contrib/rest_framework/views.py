from rest_framework import serializers
from rest_framework.generics import ListAPIView

from helsinki_notification.contrib.rest_framework.fields import TranslatedField
from helsinki_notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    content = TranslatedField()
    external_url = TranslatedField()
    external_url_title = TranslatedField()
    title = TranslatedField()
    type_name = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            "id",
            "modified_at",
            "type_name",
            "title",
            "content",
            "external_url",
            "external_url_title",
        ]

    def get_type_name(self, obj):
        return obj.type_name


class NotificationList(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.valid_objects.all()

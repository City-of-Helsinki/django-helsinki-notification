from rest_framework import serializers

from helsinki_notification.utils import map_translated_field


class TranslatedField(serializers.Field):
    def get_attribute(self, instance):
        return instance

    def to_representation(self, value):
        return map_translated_field(value, self.field_name)

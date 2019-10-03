from rest_framework import serializers

from .models import UrlObject, RequestHistory


class UrlObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UrlObject
        fields = ('url', 'interval')


class RequestHistorySerializer(serializers.HyperlinkedModelSerializer):
    url_object = UrlObjectSerializer()

    class Meta:
        depth = 1
        model = RequestHistory
        fields = ('response', 'duration', 'created_at', 'url_object')

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import UrlObject, RequestHistory
from .serializers import UrlObjectSerializer, RequestHistorySerializer


class UrlObjectViewSet(viewsets.ModelViewSet):

    serializer_class = UrlObjectSerializer
    queryset = UrlObject.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def history(self, request, *args, **kwargs):
        instance = self.get_object()
        queryset = RequestHistory.objects.filter(url_object_id=instance.id)
        serializer = RequestHistorySerializer(queryset, many=True)
        return Response(serializer.data)

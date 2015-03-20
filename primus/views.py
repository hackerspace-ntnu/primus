from rest_framework import viewsets

from rest_framework.response import Response

from primus.models import Contest

from primus.serializers import ContestSerializer


class ContestViewSet(viewsets.ModelViewSet):
    model = Contest

    def get_serializer_class(self):
        return ContestSerializer

    def get_queryset(self):
        return Contest.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

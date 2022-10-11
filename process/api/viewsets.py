from rest_framework import viewsets
from process.api.serializers import ProcessSerializer
from process.models import Process, Parts

class ProcessViewsets(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
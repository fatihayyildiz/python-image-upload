from rest_framework.viewsets import ModelViewSet

from core.models import Leave
from leaves.api.serializers import LeaveSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class LeaveViewset(ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    parser_classes = [MultiPartParser, FormParser]


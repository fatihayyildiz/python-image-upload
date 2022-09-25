from rest_framework.viewsets import ModelViewSet

from core.models import Image
from .serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class ImageViewset(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

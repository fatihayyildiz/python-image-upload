from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from core.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'user',
            'name',
            'image',
            'width',
            'height',
            'url',
            'alt',
        ]

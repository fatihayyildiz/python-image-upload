from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from core.models import Leave

class LeaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leave
        fields = [
            'user',
            'image',
            'leave_type',
            'leave_start_date',
            'leave_end_date',
            'leave_start_time',
            'leave_end_time',
            'leave_reason',
            'days'
        ]

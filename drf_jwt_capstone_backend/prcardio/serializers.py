from rest_framework import serializers
from .models import PRCardio


class PRCardioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRCardio
        fields = ['id', 'date', 'activity', 'distance', 'time', 'user']
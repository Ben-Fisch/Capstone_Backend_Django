from rest_framework import serializers
from .models import Cardio


class CardioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardio
        fields = ['date', 'activity', 'distance', 'time']

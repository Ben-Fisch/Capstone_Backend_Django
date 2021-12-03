from rest_framework import serializers
from .models import Cardio


class CardioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardio
        fields = ['id','date', 'activity', 'distance', 'time', 'user']

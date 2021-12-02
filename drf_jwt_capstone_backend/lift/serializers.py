from rest_framework import serializers
from .models import Lift


class LiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lift
        fields = ['date', 'activity', 'reps', 'weight']
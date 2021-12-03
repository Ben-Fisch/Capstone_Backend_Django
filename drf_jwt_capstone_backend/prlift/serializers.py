from rest_framework import serializers
from .models import PRLift


class PRLiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRLift
        fields = ['id', 'date', 'activity', 'reps', 'weight', 'user']
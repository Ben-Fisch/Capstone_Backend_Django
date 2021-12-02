from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Cardio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    activity = models.CharField(max_length=20)
    distance = models.IntegerField()
    time = models.IntegerField()

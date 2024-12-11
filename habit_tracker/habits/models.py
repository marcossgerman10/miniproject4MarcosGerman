from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    streak = models.IntegerField(default=0)
    last_completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

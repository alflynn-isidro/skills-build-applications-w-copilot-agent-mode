from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('run', 'Run'),
        ('cycle', 'Cycle'),
        ('swim', 'Swim'),
        ('walk', 'Walk'),
        ('other', 'Other'),
    ]
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    timestamp = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)

class Leaderboard(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

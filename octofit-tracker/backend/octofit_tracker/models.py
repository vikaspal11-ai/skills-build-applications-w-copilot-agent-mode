from django.db import models

# User Profile
class UserProfile(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    workouts = models.JSONField(default=list)

# Team
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

# Activity
class Activity(models.Model):
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    calories = models.IntegerField()
    date = models.DateTimeField()

# Leaderboard
class Leaderboard(models.Model):
    user_id = models.CharField(max_length=100)
    score = models.IntegerField()
    rank = models.IntegerField()

# Workout Suggestion
class WorkoutSuggestion(models.Model):
    user_id = models.CharField(max_length=100)
    suggestions = models.JSONField(default=list)

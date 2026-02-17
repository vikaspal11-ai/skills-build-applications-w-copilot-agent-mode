from django.test import TestCase
from .models import UserProfile, Team, Activity, Leaderboard, WorkoutSuggestion

class UserProfileTestCase(TestCase):
    def test_create_user_profile(self):
        user = UserProfile.objects.create(user_id='u1', name='Test User', email='test@example.com')
        self.assertEqual(user.name, 'Test User')

class TeamTestCase(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Team A')
        self.assertEqual(team.name, 'Team A')

class ActivityTestCase(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_id='u1', activity_type='run', duration=30, calories=200, date='2026-02-17')
        self.assertEqual(activity.activity_type, 'run')

class LeaderboardTestCase(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(user_id='u1', score=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)

class WorkoutSuggestionTestCase(TestCase):
    def test_create_workout_suggestion(self):
        suggestion = WorkoutSuggestion.objects.create(user_id='u1', suggestions=['Pushups', 'Squats'])
        self.assertEqual(len(suggestion.suggestions), 2)

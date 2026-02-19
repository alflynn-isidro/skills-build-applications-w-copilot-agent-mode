from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc', suggested_for='all')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')
    def test_user_email(self):
        self.assertEqual(self.user.email, 'test@example.com')
    def test_activity_type(self):
        self.assertEqual(self.activity.type, 'run')
    def test_workout_name(self):
        self.assertEqual(self.workout.name, 'Test Workout')
    def test_leaderboard_score(self):
        self.assertEqual(self.leaderboard.score, 100)

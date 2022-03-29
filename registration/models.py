from django.db import models
from accounts.models import UserProfile


class TeamRegistration(models.Model):
    SPORT_CHOICES = (
        ('1', 'Athletics'),
        ('2', 'Badminton'),
        ('3', 'Basketball'),
        ('4', 'Chess'),
        ('5', 'Cricket'),
        ('6', 'Football'),
        ('7', 'Table Tenis'),
        ('8', 'Tenis'),
        ('9', 'Volleyball'),
        ('10', 'Squash'),
    )
    teamId = models.CharField(max_length=15, unique=True, blank=True, null=True)
    sport = models.CharField(max_length=2, choices=SPORT_CHOICES)
    college = models.CharField(max_length=128)
    captian = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.teamId

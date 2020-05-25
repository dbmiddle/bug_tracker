from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    # user_name = models.CharField(max_length=50, null=True, blank=True)
    pass


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    filing_user = models.ForeignKey(MyUser, related_name='filing_user', blank=True, on_delete=models.CASCADE, null=True)
    assigned_user = models.ForeignKey(MyUser, related_name='assigned_user', blank=True, on_delete=models.CASCADE, null=True)
    completing_user = models.ForeignKey(MyUser, related_name='completing_user', blank=True, on_delete=models.CASCADE, null=True)
    NEW = 'NEW'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'
    INVALID = 'INVALID'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In_Pogress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    ]
    status = models.CharField(
        max_length=11, choices=STATUS_CHOICES, default=NEW)

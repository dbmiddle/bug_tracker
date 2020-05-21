from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    user_name = models.CharField(max_length=50, null=True, blank=True)


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    filing_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    NEW = 'NE'
    IN_PROGRESS = 'IN'
    DONE = 'DN'
    INVALID = 'IN'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Pogress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    ]
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=NEW)


from django.db import models
from django.utils import timezone

class ActivityLog(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    activity_type = models.CharField(max_length=50)
    details = models.TextField(blank=True)

class Screenshot(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    image_path = models.CharField(max_length=255)
    is_blurred = models.BooleanField(default=False)

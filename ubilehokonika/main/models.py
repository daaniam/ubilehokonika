from django.db import models
import uuid
from datetime import datetime


# Create your models here.

class GlobalSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_of_announcements = models.IntegerField()


class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cs = models.CharField(max_length=400)
    en = models.CharField(max_length=400, blank=True)
    de = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.cs

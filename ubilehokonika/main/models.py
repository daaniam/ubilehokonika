from django.db import models
import uuid


class GlobalSettingsModel(models.Model):
    key = models.CharField(max_length=48, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    value = models.CharField(max_length=200, blank=False)


class AnnouncementModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cs = models.CharField(max_length=400)
    en = models.CharField(max_length=400, blank=True)
    de = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.cs

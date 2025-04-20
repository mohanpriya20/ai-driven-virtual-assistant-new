from django.db import models

class DetectionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    detected = models.JSONField()
    caption = models.TextField()
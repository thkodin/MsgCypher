from django.db import models


# Create your models here.
class UserMessage(models.Model):
    """Message model."""

    message = models.CharField(max_length=120, blank=False, null=False)

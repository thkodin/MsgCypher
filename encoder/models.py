from django.db import models

from .constants import MAX_MESSAGE_LENGTH


# Create your models here.
class UserMessage(models.Model):
    """Message model."""

    message = models.CharField(max_length=MAX_MESSAGE_LENGTH, blank=False, null=False)

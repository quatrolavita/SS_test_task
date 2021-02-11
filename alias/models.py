from djongo import models
from django.utils import timezone


class Alias(models.Model):

    alias = models.CharField(blank=False, max_length=40)
    target = models.SlugField(max_length=24, blank=False)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=None)

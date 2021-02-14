from django.db import models
from django.utils import timezone
from .managers import AliasManager


class Alias(models.Model):
    """Stores a single Alias object

        Attributes:
            alias (str): Alias for target
            target (str): Target name
            start (obj: 'datetime'): Start of alias (default: stores current time)
            end (obj: 'datetime'): End of alias (default: stores None)

            objects: Manager attribute, through it you cat access custom manager method
    """

    alias = models.CharField(blank=False, max_length=40)
    target = models.SlugField(max_length=24, blank=False)
    start = models.DateTimeField(default=timezone.now())
    end = models.DateTimeField(default=None, null=True)

    objects = AliasManager()

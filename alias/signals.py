from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Alias
from .exceptions import TimeOverlapError, InvalidTimeError


@receiver(pre_save, sender=Alias)
def validate_alias(sender, instance, **kwargs):

    print('some massage')
    if instance.start > instance.end:
        raise InvalidTimeError

    alias_for_target = Alias.objects.filter(target=instance.target)

    if len(alias_for_target) == 0:
        return

    similar_alias = Alias.objects.filter(alias=instance.alias, target=instance.target)

    if len(similar_alias) == 0:
        return

    if instance.end is None:

        for similar_obj in similar_alias:

            if similar_obj.end is None:
                raise TimeOverlapError

            if (similar_obj.start >= instance.start) and \
                    (instance.start < similar_obj.end):
                raise TimeOverlapError

            if instance.start >= similar_obj.start:
                raise TimeOverlapError

            else:
                return

    for similar_obj in similar_alias:

        if similar_obj.end is None:

            if similar_obj.start >= instance.start or \
                    instance.end:
                raise TimeOverlapError

            else:
                return

        if similar_obj.start > instance.start and \
                instance.start < similar_obj.end:
            raise TimeOverlapError

        if similar_obj.start > instance.end and \
                instance.end < similar_obj.end:
            raise TimeOverlapError

        if instance.end < similar_obj.start:
            return

        if similar_obj.end <= instance.start:
            return








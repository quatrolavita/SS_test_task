from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Alias
from .exceptions import AliasTimeOverlapError, AliasInvalidTimeError


@receiver(pre_save, sender=Alias)
def alias_time_validation(sender, instance, **kwargs):
    """This method validate time measurement with new Alias obj

    Params:
        sender (class): The model class.
        instance (obj): The actual instance being saved.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        None: Returns when there is no time overlapping

    Raises:

        AliasTimeOverlapError: Occur then exists time overlapping with Alias obj in db

        InvalidTimeError: Occur when attribute start in Alias object in front of attribute end


    """

    if instance.end is not None and instance.start > instance.end:
        raise AliasInvalidTimeError

    alias_for_target = Alias.objects.filter(target=instance.target)

    if len(alias_for_target) == 0:
        return

    similar_alias = Alias.objects.filter(alias=instance.alias, target=instance.target)

    if len(similar_alias) == 0:
        return

    if instance.end is None:

        for similar_obj in similar_alias:

            if similar_obj.end is None:
                raise AliasTimeOverlapError

            if (similar_obj.start >= instance.start) and \
                    (instance.start < similar_obj.end):
                raise AliasTimeOverlapError

            if instance.start >= similar_obj.start:
                raise AliasTimeOverlapError

            else:
                continue

        return

    for similar_obj in similar_alias:

        if similar_obj.end is None:

            if similar_obj.start >= instance.start:
                raise AliasTimeOverlapError

            else:
                continue

        if similar_obj.start > instance.end:
            continue

        if similar_obj.end < instance.start:
            continue

        if similar_obj.end > instance.start > similar_obj.start:

            raise AliasTimeOverlapError

        if similar_obj.end > instance.end > similar_obj.start:

            raise AliasTimeOverlapError

        if instance.start < similar_obj.start < instance.end:
            raise AliasTimeOverlapError

        if instance.start == similar_obj.start:
            raise AliasTimeOverlapError

from django.db.models import Manager


class AliasManager(Manager):

    def get_aliases(self, target, _from, to):
        return super().get_queryset().filter(target=target, start=_from, end=to)

    def alias_replace(self, existing_alias, replace_at, new_alias_value):
        try:
            return super().get_queryset().get(alias=existing_alias).update(alias=new_alias_value, end=replace_at)

        except self.model.MultipleObjectsReturned:

            return super().get_queryset().filter(alias=existing_alias).update(alias=new_alias_value, end=replace_at)

        except self.model.DoesNotExist:

            return super().create(alias=new_alias_value, start=replace_at, end=None)

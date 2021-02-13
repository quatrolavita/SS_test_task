from django.db.models import Manager


class AliasManager(Manager):

    def get_aliases(self, target, _from, to):
        return super().get_queryset().filter(target=target, start=_from, end=to)

    def alias_replace(self, existing_alias, replace_at, new_alias_value):
        try:
            alias_obj = super().get_queryset().filter(alias=existing_alias).update(alias=new_alias_value, end=replace_at)

            if alias_obj == 0:

                return super().create(alias=new_alias_value, start=replace_at, end=None)
            else:
                return alias_obj

        except self.model.MultipleObjectsReturned:

            return super().get_queryset().filter(alias=existing_alias).update(alias=new_alias_value, end=replace_at)



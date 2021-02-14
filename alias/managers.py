from django.db.models import Manager


class AliasManager(Manager):
    """This class extends base Manager class"""

    def get_aliases(self, target, _from, to):
        """This method return queryset of Alias objects filtered by params

        Params:

            target (str): - string to slug of other models/apps of the existing project;
            _from (obj: 'datetime'): start time of target alias assignment
            to (obj: 'datetime'): end time of target alias assignment

        Returns:
            QuerySet object filtered by params
        """

        return super().get_queryset().filter(target=target, start=_from, end=to)

    def alias_replace(self, existing_alias, replace_at, new_alias_value):
        """This method can replace end(attribute) and alias(name) of Alias object

                Params:

                    existing_alias (str): - alias that need to replace;
                    replace_at (obj: 'datetime'): new time for end
                    new_alias_value (obj: 'datetime'): alias new name

                Returns:

                    status of replacement (int): 1 - successfully replaced, 0 - fail

                    alias obj (obj: Alias): return new Alias object, when the desired one does not exist
                """
        try:
            alias_obj = super().get_queryset().filter(alias=existing_alias).update(alias=new_alias_value, end=replace_at)

            if alias_obj == 0:

                return super().create(alias=new_alias_value, start=replace_at, end=None)
            else:
                return alias_obj

        except self.model.MultipleObjectsReturned:

            return super().get_queryset().filter(alias=existing_alias).update(alias=new_alias_value, end=replace_at)

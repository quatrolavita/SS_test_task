from datetime import datetime
import pytz
from django.test import TestCase
from alias.models import Alias
from alias.exceptions import TimeOverlapError, InvalidTimeError


class AliasModelTest(TestCase):

    def setUp(self):
        """Set up data before each test"""

        Alias.objects.create(alias='alias1',
                             target='target1',
                             start=pytz.utc.localize(datetime.strptime('2020-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")),
                             end=pytz.utc.localize(datetime.strptime('2021-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")))

        Alias.objects.create(alias='alias2',
                             target='target2',
                             start=pytz.utc.localize(datetime.strptime('2020-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")))

    def test_create_alias_before_similar(self):

        _from = pytz.utc.localize(
                                 datetime.strptime('2018-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f"))
        to = pytz.utc.localize(
                                 datetime.strptime('2019-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f"))
        alias_obj = Alias.objects.create(alias='alias1',
                                         target='target1',
                                         start=_from,
                                         end=to)

        self.assertIsNotNone(alias_obj)
        self.assertEqual(_from, alias_obj.start)
        self.assertEqual(to, alias_obj.end)

    def test_create_alias_after_similar(self):

        _from = pytz.utc.localize(
                                 datetime.strptime('2022-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f"))
        to = pytz.utc.localize(
                                 datetime.strptime('2023-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f"))
        alias_obj = Alias.objects.create(alias='alias1',
                                         target='target1',
                                         start=_from,
                                         end=to)

        self.assertIsNotNone(alias_obj)
        self.assertEqual(_from, alias_obj.start)
        self.assertEqual(to, alias_obj.end)

    def test_create_alias_with_overlap_err(self):

        with self.assertRaises(TimeOverlapError) as err:
            Alias.objects.create(alias='alias1',
                                 target='target1',
                                 start=pytz.utc.localize(
                                     datetime.strptime('2021-05-01 05:23:47.657263', "%Y-%m-%d %H:%M:%S.%f")),
                                 end=pytz.utc.localize(
                                     datetime.strptime('2022-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")))

        with self.assertRaises(TimeOverlapError) as err:
            Alias.objects.create(alias='alias1',
                                 target='target1',
                                 start=pytz.utc.localize(
                                     datetime.strptime('2019-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")),
                                 end=pytz.utc.localize(
                                     datetime.strptime('2022-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")))

        with self.assertRaises(TimeOverlapError) as err:
            Alias.objects.create(alias='alias1',
                                 target='target1',
                                 start=pytz.utc.localize(
                                     datetime.strptime('2020-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")),
                                 end=pytz.utc.localize(
                                     datetime.strptime('2021-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")))

        with self.assertRaises(TimeOverlapError) as err:
            Alias.objects.create(alias='alias2',
                                 target='target2',
                                 start=pytz.utc.localize(
                                     datetime.strptime('2019-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")),
                                 end=pytz.utc.localize(
                                     datetime.strptime('2021-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")))

        with self.assertRaises(TimeOverlapError) as err:
            Alias.objects.create(alias='alias1',
                                 target='target1',
                                 start=pytz.utc.localize(
                                     datetime.strptime('2021-05-01 05:23:47.657261', "%Y-%m-%d %H:%M:%S.%f")),
                                 end=pytz.utc.localize(
                                     datetime.strptime('2024-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")))

    def test_create_alias_with_invalid_time_err(self):

        with self.assertRaises(InvalidTimeError) as err:
            Alias.objects.create(alias='alias1',
                                 target='target1',
                                 start=pytz.utc.localize(
                                     datetime.strptime('2021-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")),
                                 end=pytz.utc.localize(
                                     datetime.strptime('2020-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f")))

    def test_get_aliases(self):

        _from = pytz.utc.localize(
            datetime.strptime('2020-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f"))
        to = pytz.utc.localize(
            datetime.strptime('2021-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f"))
        target = 'target1'

        alias_qs = Alias.objects.get_aliases(target=target, _from=_from, to=to)

        self.assertIsNotNone(alias_qs)
        self.assertEqual(1, len(alias_qs))
        self.assertEqual(alias_qs[0].alias, 'alias1')

    def test_aliases_replace(self):

        existing_alias = 'alias1'
        new_alias_value = 'new_alias1'
        replace_at = pytz.utc.localize(
            datetime.strptime('2021-10-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f"))

        alias_create = Alias.objects.alias_replace(existing_alias=existing_alias,
                                                   replace_at=replace_at,
                                                   new_alias_value=new_alias_value)

        self.assertIsNotNone(alias_create)
        self.assertEqual(alias_create, 1)

        alias_obj = Alias.objects.filter(alias=new_alias_value)
        self.assertEqual(alias_obj[0].alias, new_alias_value)
        self.assertEqual(alias_obj[0].end, replace_at)

        alias_create = Alias.objects.alias_replace(existing_alias='invalid alias',
                                                   replace_at=replace_at,
                                                   new_alias_value=existing_alias)

        self.assertIsNotNone(alias_create)

        alias_obj = Alias.objects.filter(alias=existing_alias)
        self.assertEqual(alias_obj[0].alias, existing_alias)
        self.assertEqual(alias_obj[0].start, replace_at)
        self.assertIsNone(alias_obj[0].end)

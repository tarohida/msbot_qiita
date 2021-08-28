import datetime
from unittest import TestCase
from IsHatsuneBirthdayService import IsHatsuneBirthdayService


class TestIsHatsuneBirthdayService(TestCase):
    def test_is_birthday(self):
        service = IsHatsuneBirthdayService()
        self.assertFalse(service.is_birthday())

    def test_is_birthday_2(self):
        service = IsHatsuneBirthdayService()
        day = datetime.datetime(2021, 8, 31, hour=0, minute=0, second=0, microsecond=0)
        service.set_date(day)
        self.assertTrue(service.is_birthday())

    def test_is_birthday_3(self):
        service = IsHatsuneBirthdayService()
        day = datetime.datetime(2021, 8, 31, hour=23, minute=59, second=59, microsecond=0)
        service.set_date(day)
        self.assertTrue(service.is_birthday())

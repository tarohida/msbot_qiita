import datetime
from unittest import TestCase
from IsHatsuneBirthdayService import IsHatsuneBirthdayService


class TestIsHatsuneBirthdayService(TestCase):
    def test_method_is_birthday_when_today_return_False(self):
        service = IsHatsuneBirthdayService()
        self.assertFalse(service.is_birthday())

    def test_method_is_birthday_when_yesterday_return_False(self):
        service = IsHatsuneBirthdayService()
        day = datetime.date(2021, 8, 30)
        service.set_date(day)
        self.assertFalse(service.is_birthday())

    def test_method_is_birthday_when_tomorrow_return_False(self):
        service = IsHatsuneBirthdayService()
        day = datetime.date(2021, 9, 1)
        service.set_date(day)
        self.assertFalse(service.is_birthday())

    def test_method_is_birthday_when_start_of_day_return_True(self):
        service = IsHatsuneBirthdayService()
        day = datetime.datetime(2021, 8, 31, hour=0, minute=0, second=0, microsecond=0)
        service.set_date(day)
        self.assertTrue(service.is_birthday())

    def test_method_is_birthday_when_end_of_day_return_True(self):
        service = IsHatsuneBirthdayService()
        day = datetime.datetime(2021, 8, 31, hour=23, minute=59, second=59, microsecond=0)
        service.set_date(day)
        self.assertTrue(service.is_birthday())

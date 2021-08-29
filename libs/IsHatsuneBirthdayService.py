from datetime import date
from HatsuneBirthday import HatsuneBirthday


class IsHatsuneBirthdayService:
    def __init__(self):
        self.birthday = HatsuneBirthday()
        self.day = date.today()

    def is_birthday(self):
        return self.is_month_equal() and self.is_day_equal()

    def is_month_equal(self):
        return self.birthday.month == self.day.month

    def is_day_equal(self):
        return self.birthday.day == self.day.day

    def set_date(self, day):
        self.day = day

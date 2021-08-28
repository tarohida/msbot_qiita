import datetime
from HatsuneBirthday import HatsuneBirthday


def utc_to_jst(datetime_utc):
    return datetime_utc.astimezone(datetime.timezone(datetime.timedelta(hours=+9)))


class IsHatsuneBirthdayService:
    def __init__(self):
        self.birthday = HatsuneBirthday()
        self.day = utc_to_jst(datetime.datetime.now())

    def is_birthday(self):
        return self.is_month_equal() and self.is_day_equal()

    def is_month_equal(self):
        return self.birthday.month == self.day.month

    def is_day_equal(self):
        return self.birthday.day == self.day.day

    def set_date(self, date):
        self.day = utc_to_jst(date)

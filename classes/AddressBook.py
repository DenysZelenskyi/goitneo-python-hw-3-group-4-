from dec.dec import input_error
from collections import UserDict
from datetime import datetime, timedelta
from collections import defaultdict
from .Record import Record


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}


    @input_error
    def add_record(self, record):
        if isinstance(record, Record): 
            self.data[record.name.value] = record
        else:
            raise ValueError("Invalid record. Please use the Record class.")

    @input_error
    def find(self, name):
        return self.data.get(name)

    @input_error
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_day_of_week_name(self, day_of_week):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[day_of_week]

    def get_birthdays_per_week(self):
        birthday_dict = defaultdict(list)
        today = datetime.today().date()
        next_week = today + timedelta(days=7)

        for name, record in self.data.items():
            if record.birthday:
                birthday_this_year = record.birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if 0 <= delta_days < 7:
                    birthday_weekday_name = self.get_day_of_week_name(record.birthday.weekday())
                    birthday_dict[birthday_weekday_name].append(name)

        return birthday_dict
from .Birthday import Birthday
from .Phone import Phone
from .Name import Name
from datetime import datetime

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, number):
        if Phone.validate_phone_number(number):
            self.phones.append(Phone(number))
        else:
            raise ValueError("Invalid phone number format. It should have 10 digits.")

    def remove_phone(self, number):
        self.phones = [phone for phone in self.phones if phone.value != number]

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                break

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone

    def __str__(self):
        phones_str = ', '.join(str(phone) for phone in self.phones)
        birthday_str = str(self.birthday.strftime("%d.%m.%Y")) if self.birthday else "Not specified"
        return f"Contact name: {self.name}, phones: {phones_str}, birthday: {birthday_str}"

    def add_birthday(self, date):
        birthday_obj = Birthday(date)
        self.birthday = birthday_obj
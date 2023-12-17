from .Field import Field

class Phone(Field):
    @staticmethod
    def validate_phone_number(number):
        if len(number) == 10 and number.isdigit():
            return True
        else:
            print("Invalid phone number format. It should have 10 digits.")
            return False
    def __init__(self, number):
        if not Phone.validate_phone_number(number):
            raise ValueError("Invalid phone number format. It should have 10 digits.")
        super().__init__(number)
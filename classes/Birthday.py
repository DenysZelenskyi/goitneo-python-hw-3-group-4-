from typing import Any
import re
from datetime import datetime


class Birthday:
    def __init__(self, birthday=None):
        self.birthday = None

        if birthday is not None and not self.validate_birthday(birthday):
            raise ValueError(
                "Invalid birthday format. It should have the format DD.MM.YYYY."
            )

    def validate_birthday(self, birthday):
        try:
            self.birthday = datetime.strptime(birthday, "%d.%m.%Y").date()
            return True
        except ValueError:
            return False

    def __str__(self):
        return (
            self.birthday.strftime("%d.%m.%Y")
            if self.birthday is not None
            else "Not defined"
        )
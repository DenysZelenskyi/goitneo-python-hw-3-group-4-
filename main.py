import collections
from datetime import datetime, timedelta
from classes.AddressBook import AddressBook
from classes.Record import Record
from dec.dec import input_error

MENU = """
    # - hello
    # - add <username> <phone>
    # - change <username> <phone>
    # - phone <username>
    # - all
    # - add-birthday <username> <birthday> (DD.MM.YYYY)
    # - show-birthday <username>
    # - birthdays
    # - "close", "exit"
"""

Person = collections.namedtuple("Person", ["name", "phone", "birthday"])


@input_error
def add_contact(person: Person, book: AddressBook):
    current_date = datetime.now().date().strftime("%d-%m-%Y")
    record = Record(person.name)
    record.add_phone(person.phone)
    book.add_record(record)
    print("Contact added.")


@input_error
def change_contact(person: Person, book: AddressBook):
    record = book.find(person.name)
    if record:
        record.edit_phone(record.phones[0].value, person.phone)
        print("Contact updated.")
    else:
        raise KeyError("Contact not found.")


@input_error
def add_birthday(person: Person, book: AddressBook):
    record = book.find(person.name)
    if record:
        # Перевірка та конвертація формату дати
        try:
            birthday_date = datetime.strptime(person.birthday, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid birthday format. It should have the format DD.MM.YYYY.")

        record.birthday = birthday_date
        print("Birthday added.")
    else:
        raise KeyError("Contact not found.")
    
def show_birthday(name, book: AddressBook):
    record = book.find(name)
    if record:
        birthday_str = record.birthday.strftime('%d.%m.%Y') if record.birthday else "Not specified"
        print(f"Contact name: {record.name}, birthday: {birthday_str}")
    else:
        print("Contact name not found.")
    
def birthdays(book: AddressBook):
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    birthdays_this_week = book.get_birthdays_per_week()

    if birthdays_this_week:
        print("Birthdays in the next week:")
        for day, names in birthdays_this_week.items():
            print(f"{day}: {', '.join(names)}")
    else:
        print("No birthdays in the next week.")


@input_error
def show_phone(name, book: AddressBook):
    record = book.find(name)
    if record:
        print(f"Contact name: {record.name}, phones: {', '.join(str(phone) for phone in record.phones)}")
    else:
        print("Contact name not found.")


def show_all(book: AddressBook):
    for name, record in book.data.items():
        print(record)


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def main():
    print(MENU)
    book = AddressBook()

    while True:
        command = input("Enter command: ").strip()
        command_name, args = parse_input(command)

        if command_name.lower() == "hello":
            print("How can I help you?")
        elif command_name.startswith("add"):
            if command_name == "add-birthday":
                add_birthday(Person(args[0], "", args[1]), book)
            else:
                add_contact(Person(args[0], args[1], ""), book)
        elif command_name.startswith("change"):
            change_contact(Person(args[0], args[1], ""), book)
        elif command_name.startswith("phone"):
            show_phone(args[0], book)
        elif command_name == "show-birthday":
            show_birthday(args[0], book)
        elif command_name == "birthdays":
            birthdays(book)
        elif command_name == "all":
            show_all(book)
        elif command_name in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()



# checking git
    
    
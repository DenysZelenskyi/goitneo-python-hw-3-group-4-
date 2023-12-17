def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Invalid input. Please provide valid data.")
            return "Invalid input. Please provide valid data."
        except KeyError:
            print("User not exist. Please provide valid data.")
            return "User not exist. Please provide valid data."
        except IndexError:
            print("Please  check your input.")
            return "Please  check your input."
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return inner
def get_card_type(number):
    number_str = ""

    for char in str(number):
        if char.isdigit():
            number_str += char

    number = number_str

    if number.startswith('4'):
        return "Visa"
    elif number.startswith('5'):
        return "MasterCard"
    elif number.startswith('37'):
        return "American Express"
    elif number.startswith('6'):
        return "Discover"
    else:
        return "Unknown"


def validate_credit_card(number):
    number_str = ""

    for char in str(number):
        if char.isdigit():
            number_str += char

    number = number_str

    if len(number) < 13 or len(number) > 16:
        return False

    total = 0
    reverse_number = number[::-1]

    for i in range(len(reverse_number)):
        digit = int(reverse_number[i])

        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit

    return total % 10 == 0


def check():
    number = input("Enter a credit card number: ")

    if validate_credit_card(number):
        print("Credit card number is valid.")
        print("Card type:", get_card_type(number))
    else:
        print("Credit card number is invalid.")


check()


def max_num(user_input):
    numbers_list = user_input.split()

    if not numbers_list:
        return "Error: Please enter only numbers separated by spaces."

    integer_numbers = []

    for num in numbers_list:
        if num.isdigit():
            integer_numbers.append(int(num))
        else:
            return "Error: Please enter only numbers separated by spaces."

    return max(integer_numbers)


user_input = input("Enter a list of numbers separated by spaces: ")
result = max_num(user_input)
print(result)


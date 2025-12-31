def min_num(numbers):
    numbers = numbers.split()

    if not numbers:  
        return "Error: Input must contain only numbers."

    try:
        smallest = min(numbers, key=int)
        return int(smallest)  
    except ValueError:
        return "Error: Input must contain only numbers."


x = input("Enter a list of numbers: ")
result = min_num(x)
print(result)


def is_prime_and_palindrome(number):

    
    if number <= 1:
        return False

    
    for counter in range(2, number):
        if number % counter == 0:
            return False

    
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    
    if original_number == reversed_number:
        return True
    else:
        return False



number = int(input("Enter a number: "))


if is_prime_and_palindrome(number):
    print("The number is both PRIME and PALINDROME.")
else:
    print("The number is NOT both prime and palindrome.")


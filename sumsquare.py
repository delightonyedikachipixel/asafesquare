def square_and_sum(numbers):
    nums = numbers.split()
    total = 0

    for n in nums:
        total += int(n) ** 2

    return total


x = input("Input a list of numbers: ")
result = square_and_sum(x)
print(result)



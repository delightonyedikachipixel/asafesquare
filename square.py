def squared_list(numbers):
    nums = numbers.split()
    squares = []

    for n in nums:
        squares.append(int(n) ** 2)

    return(squares)

x= input("input a list of numbers: ")
result = squared_list(x)
print(result)



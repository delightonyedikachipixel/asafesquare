num_total = 0

for num in range(1, 20001):
    if num % 10 == 0:
       num_total += num

print("Sum =", num_total)

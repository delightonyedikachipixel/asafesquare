

counter = 1
sum_odd = 0
sum_even = 0
count_even = 0
count_odd = 0
while(counter<=20):
    print("Enter numbers")
    number = int(input())
    if(number%2==0):
        sum_even += sum_even
        count_even += 1
        
    else:
        sum_odd += sum_odd
        count_odd += 1

    counter += 1
    
print("The sum of even numbers and sum of odd numbers and total number of odd and even numbers are",sum_even, "and",sum_odd, count_even,"and", count_odd, "respectively")

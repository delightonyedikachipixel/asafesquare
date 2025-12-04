a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

smallest=a

if smallest < b:
    smallest = b
elif smallest < c: 
    smallest = c

biggest = a
if biggest > b:
    biggest = b
elif biggest > c:
    biggest = c

else:
    print(middle)



print("increasing order:", smallest, biggest)


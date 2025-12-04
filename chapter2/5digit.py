num = int (input("Enter a five digit number: "))
a1 = num//10000
a2 = (num//1000)%10
a3 = (num//100)%10
a4 = (num//10)%10
a5 = num%10

print(a1, a2, a3, a4, a5,  sep="  ")

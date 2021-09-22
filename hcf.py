a=int(input("enter first number"))
b=int(input("enter second number"))
while a%b !=0:
    rem=a%b
    a=b
    b=rem
print("hcf is",b)

a=int(input("enter first number"))
b=int(input("enter second number"))
for m in range (1,a*b+1):
    if m%a==0 and m%b==0:
        print("lcm of number is ",m)
        break
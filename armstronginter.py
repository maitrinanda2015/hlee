lower=int(input("enter lower number"))
upper=int(input("enter upper number"))
for i in range(lower,upper+1):
    sum=0
    while(i>0):
        sum=sum+(i%10)**3
        i=i//10
    if i==sum:
        print("it is armstrong")


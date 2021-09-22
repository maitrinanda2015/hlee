n=int(input("enter a number"))
for i in range(n):
    for j in range(2*n-1):
        if i+j==3 or j-i==3:
            print("*",end="  ")
        elif i==n-1 and j % 2==0:
            print("*",end=" ")
        else: 
            print(" " ,end=" ")
    print()
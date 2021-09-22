num=int(input("enter the number"))
if num>2:
    for i in range(2,num):
        if (num%i)==0:
            print("it is not a prime number")
            print(i,"times",num//i,"is",num)
            break
        else:
            print(num," is a prime number")
    else:
        print(num,"is not a prime number")



u=int(input("beginning of interval"))
v=int(input("end of interval"))

for num in range(u,v+1):
    if num>1:

     for i in range(2,num):
       if num%i==0:
           break
     else:
         print("prime")
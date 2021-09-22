L2 = ["Bipin","Suman","Pinki","Umesh","Malati",['Shiv','Kartik','Maitri','Bipin']]
count=0
for i in (L2):
    
    if i==L2[5]:
        for k in i:
            print(k)
            count+=1
    else:
        print(i)
        count+=1
print(count)

    
a = [1,3,4,5,2,10,8,19,0]
 
for i in range(0 , len(a)):
    key = i
    for j in range(i+1, len(a)):
        if a[key] > a[j]:
            key = j
             
    a[i],a[key] = a[key],a[i]     
print(a)
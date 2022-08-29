a = [ 1 ,240, 4,1,10,12,100 , 2, 6]
maxx = a[0]

for i in range ( 0 , len(a)):
    if a[i] > maxx:
        maxx = a[i] 
print(maxx)
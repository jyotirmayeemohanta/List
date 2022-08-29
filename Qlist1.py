list=["red","blue","green","ornge"]
i=0
a=[]
while i<len(list):
    j=0
    b=[]
    while j<len(list[i]):
        b.append(list[i][j])
        j+=1
    a.append(b)
    i+=1
print(a)
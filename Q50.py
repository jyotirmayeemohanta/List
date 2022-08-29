a=[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
b=[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
i=0
c=[]
while i<len(a):
    while i<len(b):
        d=a[i]+b[i]
        c.append(d)
        i+=1
    print(c)


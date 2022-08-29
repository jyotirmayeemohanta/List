list1=[1,2,5,9,3,0]
i=0
list2=[]
while i<len(list1)/2:
    list2.append(list1[i])
    i=i+1
a=len(list1)-1
while a>=len(list1)/2:
    list2.append(list1[a])
    a=a-1
print(list2)
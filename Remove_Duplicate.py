# a=[0,0,1,1,1,2,2,3,3,4]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)


a = [1,1, 2, 2, 3 , 3, 6, 6]
b = []
 
for i in a:
    if i not in b:
        b.append(i)
     
print (b)
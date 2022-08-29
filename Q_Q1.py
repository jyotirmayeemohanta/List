# dict={"a":1,"b":2,"c":3,"d":4}
# a={}
# for i in dict:
#     a[dict[i]]=i
# print(a)


# num=[45,60,20,30,50]
# i=0
# while i<len(num):
#     j=0
#     while j<len(num):
#         if num[i]<num[j]:
#             num[i],num[j]=num[j],num[i]
#         j+=1
#     i+=1
# print(num)

# i=65
# while i<=68:
#     j=65
#     while j<=i:
#         print(chr(j),end="")
#         j+=1
#     print()
#     i+=1

# a="J yoti"
# i=0
# b=""
# while i<len(a):
#     if a[i]==" ":
#         pass
#     else:
#         b+=a[i]
#     i+=1
# print(b)

# list=[4,5,6,3,8]     
# i=0
# while i<len(a):
#     if len(a)%2!=0:
#         b=len(a)//2
#     i=i+1
# print(b)


# list=[4,5,6,3,8]
# a=[]
# b=len(list)
# c=(b//2)
# if b%2==0:
#     a.append(list[c-1])
#     a.append(list[c])
# else:
#     a.append(list[c])
# print(a)


list=[4,5,6,1,3,2,1,8]
b=len(list)
c=(b//2)
if b%2==0:
    print(list[c-1],list[c])
else:
    print(list[c])


# a={"geetu":17,"pinky":23,"shivani":17,"jyotirmayee":21}
# for i in a:
#     for j in a:
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)


# rows = int(input("Enter Diamond Pattern Rows = "))

# print("Diamond Star Pattern") 
# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(end = ' ')
#     for k in range(0, 2 * i - 1):
#         print('*', end = '')
#     print()

# for i in range(1, rows):
#     for j in range(1, i + 1):
#         print(end = ' ')
#     for l in range(1, (2 * (rows - i) )):
#         print('*', end = '')
#     print()

pt=5
for x in range(pt,-(pt),-1):
    for y in range(1,abs(x)+1):
        print(" ",end="")
    for z in range(pt,abs(x),-1):
        print("* ",end="")
    print()




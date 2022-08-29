dict={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
l=[]
for i,j in dict.items():
    for k in j:
        d={i,k}
        l.append(d)
print(l)



# 54
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]

# dict=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# a={}
# i=0
# while i<len(dict):
#     list=[]
#     key=0
#     j=0
#     while j<len(dict[i]):
#         if j==0:
#             key=dict[i][j]
#         else:
#             list.append(dict[i][j])
#         j+=1
#     a[key]=list
#     i+=1
# print(a)








# 53
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}


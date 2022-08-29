dic={"a":{4,5,2,3,0,6},"b":{9,10}}
for i in dic:
    if type(dic[i])==type({}):
        for j in dic[i]:
            if dic[i][j]%2==0:
                print(dic[i][j])
    else:
        print(dic[i])
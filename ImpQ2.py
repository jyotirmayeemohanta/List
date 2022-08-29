list=[1,2,3,[4,5,[6]]]
i=0
sum=0
while i<len(list):
    if type(list[i]==type([])):
        j=0
        while j<len(list[i]):
            if type (list[i][i]==type([])):
                k=0
                while k<len(list[i][j]):
                    sum+=list[i][j][i]
                    k+=1
            else:
                sum+=list[i][j]
            j+=1
    else:
        sum+=list[i]
    i+=1
print(sum)
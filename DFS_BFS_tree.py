
# DFS algo
if __name__=='__main__':
    ans=[]
    exactAns=[]

    arr=[[0,1],[0,2],[0,3],[1,4],[1,5],[2,6],[3,7]]

    first=-1
    for item in arr:
        if(first==-1):
            first=item[0]
        
        endElement=item[-1]
        a=1
        tempList=[item]
        for i in range(a,len(arr)):
            a=a+1
            if(endElement in (arr[i])):
                tempList.append(arr[i])
        
        for item01 in tempList:
            for item02 in item01:
                ans.append(item02)

    for ele in ans:
        if(ele not in exactAns):
            exactAns.append(ele)

    print(exactAns)
# -------------------------------------------------------------------------


# BFS Algo

arr=[[0,1],[0,2],[0,3],[1,4],[1,5],[2,6],[3,7]]

ans=[]
exactAns=[]

for item in arr:
    for element in item:
        ans.append(element)

for ele in ans:
    if(ele not in exactAns):
        exactAns.append(ele)

print(exactAns)

a=''
b=0
for e in exactAns:
    if(b==0):
        a=a+str(e)
        b=1
    else:
        a=a+' --> '+str(e)

print(a)
# ------------------------------------------------------------------------------


List=[0,2,1,1,0,1,1,1,1,1,0,1,1]

n=len(List)

number=1

count=0
maxcount=0

for i in range(n):
    if List[i]==number:
        count=count+1

    else:
        count=0    

    if count>maxcount:
       maxcount=count

print("the longest consecutive 1 count is ", maxcount)            
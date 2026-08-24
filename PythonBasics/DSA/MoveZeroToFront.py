

List=[0,1,2,0,0,0,2,3,4,6]

i=0

j=len(List)-1

while j>i:

    while List[i]==0:
        i=i+1

    if List[j]==0:
        temp=List[j]
        List[j]=List[i]
        List[i]=temp

        i=i+1

    j=j-1          

print(List)

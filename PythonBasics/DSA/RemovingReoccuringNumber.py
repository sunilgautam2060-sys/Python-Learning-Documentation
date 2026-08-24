List=[2,2,1,3,2,3,4,1,2]
num=2
i=0
n=len(List)

while i<n: #Toolbox1

    if List[i]==num: #Toolbox2
        for j in range(i,n-1): #Toolbox3
            List[j]=List[j+1]

        n=n-1 #Toolbox4

    else:
        i=i+1 #Toolbox5

print(List[:n])
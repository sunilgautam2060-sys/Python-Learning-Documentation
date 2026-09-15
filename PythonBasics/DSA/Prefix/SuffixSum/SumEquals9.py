#the core logic of this problem is :
#we make a prefix array directly without having first value 0. 
#like:List=[1,2,3,4,5]
#prefix=[1,3,6,10,15]
#prefix array[0]=sum of List up to List[0].
#prefix array[1]=sum of List up to List[1], i.e List[0]+List[1] and so on .


List=[1,2,3,4,5]
TargetSum=9

sum=0
Prefix=[]
bool=False

for i in range(len(List)):
    sum+=List[i]
    Prefix.append(sum)

   

for i in range(len(List)):
    for j in range(i+1,len(List)):
        CurrentSum=Prefix[j]-Prefix[i]

        if CurrentSum==TargetSum:
            bool=True
            StartingIndex=i+1
            EndingIndex=j
            print("The Subarray is:")
            print(List[StartingIndex:EndingIndex+1])
            break

    if bool==True:
        break    

            
             
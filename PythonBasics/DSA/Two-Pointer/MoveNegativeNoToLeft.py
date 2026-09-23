
#The Core logic of this problem is to place i and j smartly:
#role of i=skip the list elements if they are already in right place.
#for example if list already starts with negative elements do not interfere it,
#put the i in 1st non-negative element index , 
#compare i and j now "i" is already tracking the non-negative no,
#its time to look at j only , if j is negative number than swap and increase both,
#if j is also non negative number than just increase j ,

#for example if list starts with List=[-1,-7,4,7,-3,-9] than i will keep 
#increasing until index 2 , there is non-negative number than there will be comparision and swapping ,
#as per condition.



List=[3,-2,5,-7,8,-1,4,-6] #given list.

n=len(List) #length of list.

i=0 #initial value of i.
 
j=1 #initial value of j.

while(j<n): #j keeps traversing list .

    if List[i]<0: #this will keep increasing i until it finds positive integer.
        i=i+1

    elif List[j]<0: #if j track negative number than only swap occurs

        temp=List[j]
        List[j]=List[i]
        List[i]=temp

        i=i+1

    j=j+1         #if j track positive than simple continue loop.

print(List)     #print the output.
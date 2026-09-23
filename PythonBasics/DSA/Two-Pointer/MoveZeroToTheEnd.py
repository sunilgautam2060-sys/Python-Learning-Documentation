

List=[ 3,10,0,0,1,4,0,7,0,5] #given List.


n=len(List) #length of the list.

i=0 #initializing the i.its role is to track the 0 to swap.


while(i<n and List[i]!=0): #It place the i directly to the 0 and j from next one.
                           #if the starting place is not zero .
    i=i+1

j=i+1 #its role is to traverse and bring new element if its non-zero than swap with i
      #if its zero than skip.


while(j<n):#traversing j up to n. 

    if List[j]!=0: #if the new element is non-zero than swap if not than increase j.
        temp=List[j]
        List[j]=List[i]  #swapping toolkit.
        List[i]=temp
        i=i+1

    j=j+1 #increament j .


print(List[:n]) #print final output.  



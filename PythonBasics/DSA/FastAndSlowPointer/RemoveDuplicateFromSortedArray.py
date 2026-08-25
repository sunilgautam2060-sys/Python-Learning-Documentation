


List=[1,1,1,2,3,3,4,5,5,5,5,5] #Given List.

n=len(List) #Length of list.

i=0 # i role is to check whether the new element(j) is same as me ? 
    # if yes than ignore,if no than give entry to the new element(J)in the window.


j=1 # j task is to traverse the list and introduce new element to i ,
    #so that i can verify new element is eligible to enter or not.

while j<n:#j is traversing up to n.

    if List[i]!=List[j]:#if they are different than only run this case:
        i=i+1           #First increase i , than place new eligible element in window.
        List[i]=List[j] #Now the only eligible element window is maintained from starting to i.
        

    j=j+1     #increase the j to traverse.

print(List[:i+1]) # since we only need the window from starting to i. so use 
                  #slice operator to slice the list from starting up to i only.

   


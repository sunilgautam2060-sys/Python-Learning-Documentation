

#it is like used in the condition:where the array elements range from particular value 
#like 1 to n . like: we are given an input array which value ranges from 1 to n ,
#sort that particular array than we use cyclic sort ,because we know the array element lies from particular range.

#normally sorting algorithm takes time complexity of o(nlogn) but if we know the range
#than why use the sorting algorithm which takes o(nlogn) instead use cyclic sort
#which time complexity is o(n).




List=[3,1,2,5,4] #notice the array belongs to range 1 to 9 . 

n=len(List)

i=0
while i<n:
    correct_index=List[i]-1 #this will say the correct index the list element should be actually.
                            # like hunuparney index.
    
    if correct_index!=i:  #i is aailey vako index but hunuparney chai correct_index.
         
         temp=List[i] #yedi hunuparney ra aailey vako index equal xaina vaney matra swapping.
         List[i]=List[correct_index]
         List[correct_index]=temp


    else: #else means the element are already in their correct place or index,
          #in that case do nothing continue traversing the array.
         i=i+1

print(List)              


#This is PURE cyclic sort.
#
#No negative marking.
#
#No duplicate detection.
#
#No missing detection.
#
#Just:
#
#Put every number in its home.










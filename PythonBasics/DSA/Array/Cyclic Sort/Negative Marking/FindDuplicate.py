

#the logic of negative indexing to find duplicate elements is:
#we traverse the array for each element and mark the index of that element as negative.
#because the index of the element are fixed like index of 1 is 0 ,index of 2 is 1 and so on.
#so if we traverse the array and mark the index of that element as negative than ,
#if we encounter the same element again, we will know it's a duplicate.

#if the index of that element is already marked as negative than we will know that the element is duplicate 
# and we will add it to the duplicate list.



List=[1,2,2,1,1,3,7,6,9,8,8,4,5,5]

n=len(List)

duplicate=[]

current_index=0  #we calculate the correct index of each element .

while current_index<n:

    correct_index=List[current_index]-1 #this is the formula to calculate the correct index of each element.

    if List[correct_index]>0:#if the element at the correct index is positive than we will mark it as negative.
        List[correct_index]= -List[correct_index]

    else:#if the element at the correct index is already negative than we will know that the element is duplicate .
        bool=False

        for i in range(len(duplicate)): #this loop check whether the duplicate element is already in the duplicate list or not.
            if List[current_index]==duplicate[i]:
                bool=True
                break #if element is already in duplicate list than we will break the loop and not add it again to the duplicate list.

        if bool==False: #bool will remain false if the element is not in the duplicate list and we will append it to the duplicate list.
            duplicate.append(List[current_index])


    current_index=current_index+1 #the current_index will keep traversing the array until it reaches the end of the array.

#we print the duplicate list which contains all the duplicate elements in the array.
print("Duplicate Elements are :",duplicate)            

                



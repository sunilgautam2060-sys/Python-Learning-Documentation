

#we already did this problem using negative marking but now we will do this problem using cyclic sort.
#the core logic of cyclic sort is:
#we traverse the array and for each element we calculate the correct index of that element .
#and if the current index is not equal to the correct index than we will swap the element at current index with the element at correct index.
#only if the element at correct index is not equal to the current element because if it is equal than we will know that the element is duplicate and we will add it to the duplicate list.
#so overall if current_index!=correct_index
#decision1 : if List[current_index]!=List[correct_index] than swap
#decision2 : else than add it to the duplicate list.
#if the current_index==correct_index than we will move to the next index and repeat the process until we reach the end of the array.


List = [1,3,2,7,4,6,5,2,7,8,9,3]

n = len(List)

duplicate = []

current_index = 0

while current_index < n:

    correct_index = List[current_index] - 1 #calculating correct index for each element.

    # Check whether current element is already
    # at its correct index.

    if current_index != correct_index: #if not equal than there is 2 decision to make:

        # If the correct index contains a different value,
        # swap them.

        if List[current_index] != List[correct_index]: #if element are not equal than swap.

            temp = List[current_index]
            List[current_index] = List[correct_index]
            List[correct_index] = temp

        else: #it means element at current index is equal to the element at correct index.
              # which means the same value is already occupying its correct position and we will add it to the duplicate list and move on.

            # Same value is already occupying
            # its correct position → duplicate.

            bool = False

            for i in range(len(duplicate)): #the loop checks whether the duplicate element is already in the duplicate list or not.

                if List[current_index] == duplicate[i]:#if present than trigger bool flag than break.

                    bool = True
                    break

            if bool == False:#if bool flag is not triggered at all than it means the duplicate element is not present in the duplicate list and we will add it to the duplicate list.

                duplicate.append(List[current_index])

            # IMPORTANT:
            # We have finished processing this index.

            current_index = current_index + 1 #if this decision occurs than we will move on .

    else: #if above decision is not triggered than it means the current index is already equal to the correct index and we will move on to the next index.

        current_index = current_index + 1 


#print the duplicate list which contains all the duplicate elements in the array.
print("Duplicate Elements are :", duplicate)


#START
# ↓
#Take current element
# ↓
#Calculate its correct index
# ↓
#Is current index already its correct index?
# ↓
#YES → move to next index
# ↓ NO
#Is the correct index occupied by a DIFFERENT value?
# ↓
#YES → swap
# ↓
#NO
# ↓
#Same value already exists there
# ↓
#DUPLICATE
# ↓
#Have I already stored this duplicate?
# ↓
#NO → store it
#YES → don't store again
# ↓
#Move to next index


# Cyclic Sort
# Each value has its own correct index.
# 1 -> index 0
# 2 -> index 1
# 3 -> index 2
# ...
# 9 -> index 8


#cyclic sort preassumed or fixed defined the correct position of the number like:
#1 position is 0th index , 5 position is 4th for sure its like fixed or something like that
#in so following that algorithm the array element gets placed . 

List = [1,3,2,7,4,6,5,2,7,8,9,3]

current_index = 0
DuplicateNumber = []

while current_index < len(List):

    correct_index = List[current_index] - 1

    # If the value is already present at its correct index,
    # then the current value is a duplicate.

    if List[current_index] == List[correct_index]:

        if current_index != correct_index:
            DuplicateNumber.append(List[current_index])

        current_index = current_index + 1

    else:

        # Put the value into its correct position.

        temp = List[current_index]
        List[current_index] = List[correct_index]
        List[correct_index] = temp
 

print("Sorted List :", List)
print("Duplicate Numbers :", DuplicateNumber)
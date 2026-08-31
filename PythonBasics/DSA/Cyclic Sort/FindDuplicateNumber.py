

# Cyclic Sort
# Each value has its own correct index.
# 1 -> index 0
# 2 -> index 1
# 3 -> index 2
# ...
# 9 -> index 8


List = [1,3,2,7,4,6,5,2,7,8,9,3]

i = 0
DuplicateNumber = []

while i < len(List):

    correct_index = List[i] - 1

    # If the value is already present at its correct index,
    # then the current value is a duplicate.

    if List[i] == List[correct_index]:

        if i != correct_index:
            DuplicateNumber.append(List[i])

        i = i + 1

    else:

        # Put the value into its correct position.

        temp = List[i]
        List[i] = List[correct_index]
        List[correct_index] = temp


print("Sorted List :", List)
print("Duplicate Numbers :", DuplicateNumber)
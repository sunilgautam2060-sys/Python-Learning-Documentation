List = [1, 2, 3, 2, 4, 1, 5, 3, 6]

n = len(List)

i = 0
j = 1

while j < n:

    duplicate = False

    # Checking for duplicate
    for C in range(i, j):

        if List[j] == List[C]:

            duplicate = True

            # Shifting elements to the left
            for S in range(j, n - 1):
                List[S] = List[S + 1]

            # Logical size decreases
            n = n - 1

            break

    # If no duplicate was found
    if duplicate == False:
        j = j + 1


print(List[:n])
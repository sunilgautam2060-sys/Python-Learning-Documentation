List = ["Sunil", "Pradip", "Anil", "Sunil",
        "Sita", "Pradip", "Sita", "Anil"]

n = len(List)

i = 0

while i < n:
    j = i + 1

    while j < n:

        if List[i] == List[j]:

            # Move elements one position to the left
            for k in range(j, n - 1):
                List[k] = List[k + 1]

            n = n - 1

        else:
            j = j + 1

    i = i + 1

print(List[:n])
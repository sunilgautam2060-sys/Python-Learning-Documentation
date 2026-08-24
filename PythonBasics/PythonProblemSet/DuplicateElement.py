List = [1, 2, 1, 4, 2, 3, 4]

Duplicate = []

i = 0
n = len(List)

while i < n - 1:

    j = i + 1

    while j < n:

        if List[i] == List[j]:
            Duplicate.append(j)

        j = j + 1

    i = i + 1

print(Duplicate)
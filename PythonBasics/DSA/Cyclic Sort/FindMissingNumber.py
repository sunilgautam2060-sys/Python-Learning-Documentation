


List = [3, 0, 1]

n = len(List)

i = 0

while i < n:

    correct_index = List[i]

    if List[i] < n and List[i] != List[correct_index]: #if the list[i] is not list[correct_index].
                                                    #swap toolkit.
        temp=List[i]
        List[i]=List[correct_index]
        List[correct_index]=temp

    else:

        i = i + 1
#Basically up to here it is just a cyclic sort algorithm . 


MissingNumber = n

for i in range(n):

    if List[i] != i:
        MissingNumber = i
        break


print("Missing Number :", MissingNumber)
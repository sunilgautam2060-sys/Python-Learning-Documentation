

#the main pattern and algorithm of this problem is:
#we know the target and current element we find the pair for each current element during looping.
#traversing the list , calculate pair=target-current element 
#if the pair exist in dictionary than current element and pair is the two sum.
#if not than store current element in dictionary.


List=[6,7,11,2]
Target=9
Pair=0
dictionary={}

for CurrentElement in List:
    Pair=Target-CurrentElement
    if Pair in dictionary:
        print("The Number are: ")
        print(Pair, "and" ,CurrentElement ,end=" ")
        break

    else:
        dictionary[CurrentElement]=""
        

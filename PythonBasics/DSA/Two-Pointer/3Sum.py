List = [4, 9, 16, 25, 34] #Given Lists.

n = len(List) #Length Of List.

Required = int(input("Enter The Required Three Integer Sum: ")) #Storing The Required Sum.

i = 0 # initialization of i.

while i < n - 2: # i goes from 0 to n-2 for each i. j and k traverse and check required sum.

    j = i + 1 #for each i .j starts from (i+1).
    k = n - 1 #for each i. k starts from (n-1).

    while j < k: #loop executes for each i . with condition j<k.

        Sum = List[i] + List[j] + List[k] #calculating sum.

        if Sum > Required: #sum greater than required means need to decrease sum so decrease k.
            k = k - 1

        elif Sum < Required: #sum less than required means need to increase sum so increase j.
            j = j + 1

        else:
            print("The Three Integers Are: {} {} {}".format(
                List[i], List[j], List[k]
            ))
            break #if required=sum no need to check furthur break it.

    i = i + 1 #incrementing i.

#the core logic of this problem is : we have to find the  minimum substring where ,
#a , b and c  must present in that substring window.

#that means first we satisfy our condition i.e start increasing window from 0 ,
#until we finds out the condition i.e to find the substring where a,b,c must contains
#at this point we do not care about repetition or anything we just care to satify the 
#condition where a, b and c all  are presented in our substring window.
#we will use a separate variable for count of a , b, and c .

#after that we shrink the window from left and during shrinking we will question ?
#is that the (a or b or c) ? if yes than decrease their count not than continue.
#we keep doing and we eventually finds minimum substring .



string="eaaebbdakccdadbc"

n=len(string)

MinimumSubarrayLength=n+1

i=0 #it is left window.
j=0 #it is right window.

startingindex=0
endingindex=0

CountOfa=0
CountOfb=0
CountOfc=0

while j<n: # j is right window it ,keeps traversing and bring new character in window.

    if string[j]=="a": #this code maintain the count of a .
        CountOfa+=1

    elif string[j]=="b": #this code maintain the count of b.
        CountOfb+=1

    elif string[j]=="c": #this code maintain the count of c.
        CountOfc+=1


    # Check whether current window contains a,b,c
    #we do not care about repetition more than 1 of (a ,b,c)
    #we care about (a and b and c)in our window.
    if CountOfa>=1 and CountOfb>=1 and CountOfc>=1:

        count=(j-i)+1  #calculating their window size.

        if MinimumSubarrayLength>count: #updating or tracking our current minimum everytime.

            MinimumSubarrayLength=count
            startingindex=i              #this is memory or storing the minimum till now .
            endingindex=j


        # Try making the window smaller
        #now this code responsibility is to shrink the window 
        #while shrinking it keeps track is that (a or b or c )?
        #if yes than decrease their count after that decrease are they still satisfying the condition ?
        #if yes than continue doing the shrinking process if not than increase j ,
        #bring new element to the window.

        while CountOfa>=1 and CountOfb>=1 and CountOfc>=1:

            if string[i]=="a": #if leftmost part element is "a" only than.
                CountOfa-=1

            elif string[i]=="b":#if leftmost part element is "b" only than.
                CountOfb-=1

            elif string[i]=="c":#if leftmost part element is "c" only than.
                CountOfc-=1

            i+=1 #out of above 3 only one can be true or nothing can be true so increase i .
                 # i is right window.


            #after shrinking also the condition of window maintaining (a,b and c).
            #than we should update that window to our minimum window right ? 
            #thats what we are doing.


            #this whole block is to update the shrinked window with condition satisfied
            #because shrinked window is smaller than the first window we encounter 
            # which meets condition.
            # and we need smallest window which meets condition , so we update and trace our window.
            if CountOfa>=1 and CountOfb>=1 and CountOfc>=1:

                count=(j-i)+1

                if MinimumSubarrayLength>count:  

                    MinimumSubarrayLength=count
                    startingindex=i
                    endingindex=j


    j+=1 #bringing new element to the window ,


#printing the output.
print("Minimum Subarray Length:",MinimumSubarrayLength)
print("Minimum Substring:",string[startingindex:endingindex+1])



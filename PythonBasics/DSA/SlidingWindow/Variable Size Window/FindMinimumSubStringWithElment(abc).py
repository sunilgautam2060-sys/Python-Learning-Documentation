


string="eaaebbdakccdadbc"

n=len(string)

MinimumSubarrayLength=n+1

i=0
j=0

startingindex=0
endingindex=0

while j<n:

    CountOfa=0
    CountOfb=0
    CountOfc=0

    # Count a, b and c inside current window
    for C in range(i,j+1):

        if string[C]=="a":
            CountOfa+=1

        elif string[C]=="b":
            CountOfb+=1

        elif string[C]=="c":
            CountOfc+=1


    # Check whether current window contains a,b,c
    if CountOfa>=1 and CountOfb>=1 and CountOfc>=1:

        count=(j-i)+1

        if MinimumSubarrayLength>count:

            MinimumSubarrayLength=count
            startingindex=i
            endingindex=j


        # Try making the window smaller
        while CountOfa>=1 and CountOfb>=1 and CountOfc>=1:

            if string[i]=="a":
                CountOfa-=1

            elif string[i]=="b":
                CountOfb-=1

            elif string[i]=="c":
                CountOfc-=1

            i+=1

            if CountOfa>=1 and CountOfb>=1 and CountOfc>=1:

                count=(j-i)+1

                if MinimumSubarrayLength>count:

                    MinimumSubarrayLength=count
                    startingindex=i
                    endingindex=j


    j+=1


print("Minimum Subarray Length:",MinimumSubarrayLength)
print("Minimum Substring:",string[startingindex:endingindex+1])



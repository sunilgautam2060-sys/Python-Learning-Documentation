
#the question is to find the longest substring without repeating a,b and c .

#the logic is start i and j from 0 , move j one step at a time in each j movement,
#there will be checking is it (a or b or c)? if yes than we increase the  their individual count.
#if we get in a window where a,b,c are only one time than we track or store that window.
#than we continue expanding j , if we encounter the count of (a or b or c) more than 1 time 
#than we shrink the window from left.


string="kabdfedaeabdc"
n=len(string) #Length Of String.

i=0
j=0

MaximumSubarrayLength=0

CountOfa=0 
CountOfb=0  
CountOfc=0

while j<n:

    if string[j]=="a":#checks the count of a ,and track CountOfa.
        CountOfa+=1

    elif string[j]=="b":#checks the count of b , and track CountOfb.
        CountOfb+=1

    elif string[j]=="c":#checks the count of c , and track CountOfc.
        CountOfc+=1


    if CountOfa==1 and CountOfb==1 and CountOfc==1:
     #this is the first valid window.
     #where the a,b,c occurs exactly one time so we track or trace that window.
     #we store this window information in MaximumSubarrayLength with fulfilled condition,
        
        count=(j-i)+1
        
        if MaximumSubarrayLength<count: #if any other window with size greater than this will replace .
            MaximumSubarrayLength=count
            startingindex=i
            endingindex=j


    if CountOfa > 1 or CountOfb > 1 or CountOfc > 1:#this will shrink if count of a or b or c exceeds by 1 , 
         
        while CountOfa>1 or CountOfb>1 or CountOfc>1:

            if string[i]=="a":
                CountOfa-=1

            elif string[i]=="b":
                CountOfb-=1

            elif string[i]=="c":
                CountOfc-=1


            i+=1


    j=j+1

print("The maximum subarray length without repeating abc is " , MaximumSubarrayLength)
print("They are:")
print(string[startingindex:endingindex+1])                        




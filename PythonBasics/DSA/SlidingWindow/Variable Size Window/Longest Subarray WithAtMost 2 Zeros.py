
#this is variable size sliding window problem , i have to find the longest subarray
#with specific condition which is at most 2 zero is eligible in subarray .
#basically find longest subarray with at-most 2 zero . 


List = [1,1,0,1,0,0,1,1,1,0]

n = len(List)

LongestSubarraySize = 0
count = 0  #we use count variable to count zero if count is less than or equal to 2 ,its fine
           #keep adding element in window but if it exceed than 2 we need to shrink the window ,
           #until it become 2 or less . 

startingindex = 0
endingindex = 0

i = 0
j = 0

while j < n: #start traversing basically it is rightwindow.

    if List[j] == 0:  #if we encounter 0 , than count the no.of zero as per our requirement.
        count += 1

    while count > 2: #if count exceed 2 than shrink the element from left , but shrink should remove the zero
                     #if not than it is useless so we keep increasing i ,until we throw zero,

        if List[i] == 0:
            count -= 1

        i += 1

    windowsize = (j-i)+1  #size of window.

    if windowsize > LongestSubarraySize:
        LongestSubarraySize = windowsize   #this block will keep on tracking the subarray 
                                           #which fits the condition one by one.
        startingindex = i
        endingindex = j

    j += 1   #the right window is increamented by one to keep traversing the array . 


#printing the result.
print("The longest subarray with at most 2 zeros is:")
print(List[startingindex:endingindex+1])
print("And their size is:", LongestSubarraySize)
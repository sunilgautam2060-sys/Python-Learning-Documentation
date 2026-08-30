
#this problem belongs to variable size sliding window , the question demands us to find
#longest subarray with sum<=5 . 
#the core logic is :keep adding the element in window until the sum is less than or equal to 5
#if the sum exceed 5 , keep subtracting the window by leftmost element until the eligible window which is 
#sum<=5.



List =[1, 2, 1, 1, 3, 2, 1]

k=5  # the sum should be less than or equal to K . 

n=len(List)

sum=0  #initializing sum with 0 . 

i=0 #start of the window.

j=0 #end of the window . 

LongestSubarray=0
startingindex=0
endingindex=0

while j<n: #j task is to keep traversing the array and bring new element to window.
    sum=sum+List[j] #we keep adding 
    j=j+1

    if sum<=k: #we need longest subarray with sum<=k so we need to track .

        count=(j-i) #this block is to store the length of subarray with condition sum<=5.

        if LongestSubarray<count:
            LongestSubarray=count     #this block is to track the subarray with required condition. 
            startingindex=i
            endingindex=j-1


    else: #this block shrink the window if the sum exceed 5 . 
        while(sum>k):  #it shrink until the sum>5 by subtracting leftmost part continously until sum>5. 
            sum=sum-List[i]
            i=i+1


#printing
print("The Longest subarray count is ", LongestSubarray)   
print("They are :")
print(List[startingindex:endingindex+1])    





                    


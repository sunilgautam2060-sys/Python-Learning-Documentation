#the problem named:MaximumSumSubarrayOfSizeAtMostK means find the maximum sum of subarray,
#but the constraints is we are only eligible to use the subarray less than or equal to K.
#not more than that means if K=4 ,out of subarray of size 1 or 2 or 3 or 4 find the maximum sum .
#for this particular problem we use kadanes algorithm rather than sliding window because sliding window with variable size subarray.
#will fail because of negative elements . 
#here we initialize current_sum and maximum_sum=list[0] and starts traversing from 1 to n-1.
#if the next element in list i.e list[1] is greater than current_sum+list[1] ,current_sum=list[1].
#if not than current_sum=current_sum+list[1] this is the heart of kadanes algorithm.

#the new thing in this problem is to maintain the window not greater than size k , 
#so before updating maximum_sum we check if the size of current_sum is really less or equal to k ?
#if not than we delete the left most part of the subarray and add new element in right .
#in this way we will maintain the required window plus maximum will also be saved below.




List=[1,-19,22,-5,7,-9] #initializing the list.

n=len(List)#size of the list.

Current_sum=List[0] #initializing the current_sum=List[0]. 

k=3 #this is the most K value we , are eligible to keep the subarray window of maximum 3.

Maximum_sum=List[0] #initializing the maximum_sum=List[0] ,even the current_sum will keep on changing window but 
                    #maximum will only gets updated only if current_sum>maximum_sum . 

start=0 #initializing the i tracking variable with 0

for i in range(1,n): #traversing starts from 1 to n-1.

    if Current_sum+List[i]<List[i]: #case1:if this than

     Current_sum=List[i] #current_sum will be this means new individual window.

     start=i #for tracking starting index .


    else:    
       Current_sum=Current_sum+List[i] #case2:if not than this for sure ,if this statement is true
                                       #than no need to worry about starting index because its same.


    if (i-start)+1>k: #this condition is here to remove the extra window element this only work when window elements
                      #is greater than k.
       Current_sum=Current_sum-List[start] #this is the code to remove leftmost part of the window.
       start=start+1 #if left most part gets deleted than start should increase by 1 for sure.


    if (Current_sum>Maximum_sum): #now this is the toolkit which task is to compare current_sum
                                  #and maximum_sum and update the maximum_sum
       Maximum_sum=Current_sum    #if only current_sum>maximum_sum the maximum_sum will be replaced by current_sum.
       Starting_index=start       #this is to track the starting index .
       Ending_index=i             #this is to track the ending index.



#this is to print the final output .
print("The maximum subarray sum of size at most k is : " , Maximum_sum)
print("The index starts from {} and ends at {}".format(Starting_index,Ending_index))       

       
       
       


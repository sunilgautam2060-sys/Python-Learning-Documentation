
#the overall logic of range-sum query is we have to find the sum of elements from the particular range.
#range includes the elements from left to right out of total array/list elements.
#what is its important ? if we do not maintain prefix/suffix array the range sum need to be calculated,
#by adding each array elements inside it every single time traversing the  array ,everytime we query.
#but if we maintain prefix/suffix array it will take o(n)time to make prefix/suffix array at start ,
#but after that each query we do, it will use prefix/suffix array instead of traversing the array elements through loops in each query.
#And finding the range-sum through prefix/suffix array will only take o(1)time.

#final thing to remember the length of prefix/suffix array is 1 more because they start with 0 . 


List = [3,1,4,2,5] #given list.

n = len(List) #length of the list.

left = int(input("Enter the left index: ")) #ask user for left index .
right = int(input("Enter the right index: "))#ask user for right index .
                                             #now at we have both left and right index.
                                             #this is the range and we do sum of it so it is called as range-sum-query problem.

prefix = [0] * (n + 1) # prefix array initialization , there is (n+1)because the starting index is 0.
                       # and prefix[n+1] means the lenght of prefix/suffix array length will be 1 more than the given list/array
                       #because they starts with 0 . another things the (n+1) is length not last index ,last index is prefix[n]
                       #prefix[n] means sum of list from 0 to (n-1) so basically sum of all element of list . 

for i in range(n):#i starts from 0 ends at n-1.
    prefix[i+1] = prefix[i] + List[i] #core logic to get prefix sum array.

string = input("Should left and right index be included? ") #this string will store either "yes" or "no".

if string == "yes": #if yes only than.

    total = prefix[right+1] - prefix[left] #logic to get range sum with inclusive index.

    print("The sum from L to R including them is:", total)#displaying result.

else:#if no only than .

    total = prefix[right] - prefix[left+1] #logicc to get range sum with exclusive index.

    print("The sum from L to R excluding them is:", total) #displaying result .
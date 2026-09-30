
#Here is the logic of the PivotIndex ,instead of creating separate two arrays of,
#prefix array and suffix array ,we solve the problem using left and right variable.
#left variable role is to add all the left most part which can be written in code easily.
#whenever we traverse a given list we initialize left=0 and starts traversing the list.
#from index 1 to calculate the left in index 1 we use general formula or pattern:
# left=left+a[i-1] since we start traversing from 1 the first index 1 produce :
# left=0+a[0]=0+1=1 and index 2 produce left=1+7=8 and so on left side is responsible to ,
#add all the element in left part . 

#for right variable its slightly different ,right variable simply means adding the 
#right side of the index .suppose List size is 6 , we are at index 2 ,left variable
#means sum of list[0]+list[1] excluding 2 , whereas right variable is :list[3]+list[4]+list[5].
#to calculate right variable for each traversing index , we use the formula or pattern:
# right=SumOfListElement-(left+List[i]).lets vizualize it 
#suppose your list last index is 5 , you are at index 3 , to calculate right variable
#you need to substract left part  and list[3] out of total sum , to get right variable
#thats it .




List=[1,7,3,6,5,6] # given List.

n=len(List) #Length of list.

left=0 #its role is to sum left part within i-1.

sum=0 #its role is to sum the list so that right can be calculated.

right=0 #its role is to sum the right part from i+1 to n-1.

for s in range(n): #here's the loop to sum the list elements.
    sum+=List[s]   # here  the actual sum logic.


for i in range (1,n): #now traverse from 1 to n-1 .
    left+=List[i-1]   #at each index from 1 to n-1 , calculate left and right part.
    right=sum-(List[i]+left) #its right part.

    if left==right: #if left part and right part is equal only than.return the i or index.
        print("The Index Where Prefix Sum Equals Suffix Sum is  " , i)
        break # this is necessary after finding pivot index break from loop 

         
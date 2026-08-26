
#the core objective is to write the concept of suffix sum in code form , it does not mean
#suffix sum problem will be solve calculating suffix array everytime.


 #the core logic of this code is to calculate the suffix sum array or list,from the given list.
 #suffix sum generally means right part sum suppose the last index of list is 5,
 #i am at 3 index suffix sum means sum of list[4]+list[5] thats it , 
 #to make suffix sum array , we initialize the suffix[n-1]=0 because the suffix sum of list[n-1]=0,
 #because there is nothing on the right to sum so its 0 . 
 #to calculate the suffix sum array we use the formula:
 # suffix[i]=suffix[i+1]+List[i+1] , one important note:
 # here the i starts from (n-2) and ends at 0 index . because we calculate suffix array from right side.



List=[1,2,3,4,5] #given list.

n=len(List)      #length of list.

suffix=[0]*n     #initializing suffix array of size n with value 0 .

for i in range(n-2,-1,-1): #traversing from (n-2) to 0 , decresing 1 at a time.
    suffix[i]=suffix[i+1]+List[i+1] #calculates the suffix array with genral formula.

print(suffix[:n])    #prints the suffix sum array.

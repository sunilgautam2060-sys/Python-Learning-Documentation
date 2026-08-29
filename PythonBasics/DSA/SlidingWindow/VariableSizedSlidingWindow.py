

#The actual problem name is :find minimum sized window with sum<=7.
#These type of problem is solved used variable size sliding window.

List=[2,3,1,6,4,3,7]

n=len(List)

minimumsizesubarray=n+1 #we try to put its value maximum since the maximum subarray size is 
                        #size of array itself so we put it value +1 

k=7 #this is given constraint 

sum=0 #this variable is used to calculate sum . 

i=0 #i is start of window.
j=0 #j is end of window.

startingindex=0 #this variable is to store the  starting index.
endingindex=0   #this variable is to store the ending index.

while j<n:

    sum=sum+List[j] #keep on adding until the constraint K . 
    j=j+1
  

    while sum>=k:  #this is after meeting the constraint now
                   #this keep squeezing the window to meet the constraint with minimum subarray.
        
        count=j-i  #this is to calculate length of window.

        if count<minimumsizesubarray: #this is used to update the minimum window.
            minimumsizesubarray=count
            startingindex=i
            endingindex=j-1

        sum=sum-List[i] #this keeps removing the left most part 
        i=i+1           #this track aftewards.

#print final result to screen.
print("The minimum size subarray of sum 7 is " , minimumsizesubarray)
print("the subarray starts from :" , startingindex)
print("the subarray ends at : " , endingindex)    



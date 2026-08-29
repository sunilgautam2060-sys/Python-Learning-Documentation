

List=[-7,3,-1,4,2,-3]#This is the Given List.

n=len(List)#Length of a list.

Max=0#Initializing Max with 0.

for i in range(n):#Start of the subarray is track by i , it gets gradually increase

    sum=0 #we initialize the sum with 0 after every new subarray Starting.

    for j in range(i,n):#J tracks the ending of a subarray it gets gradually increase whereas i is stable at start
                           #j will keep on adding  element in  subarray .
        
        sum=sum+List[j]#This will calculate the sum of subarray .

        if sum>Max:#if only the sum is greater than max, this statement will run.

         Max=sum #if sum is greater than max than replace max with sum.

         StartingIndex=i #since the  new maximum subarray sum arrived just now , 
                         #so lets track their starting .
         
         EndingIndex=j #so lets track their ending index.


#Basic Printing Demonstration Of the Above Calculated Values.
print("The Maximum  Subarray Sum is :" , Max)
print("The Subarray Starts From : " , StartingIndex)
print("The Subarray Ends At : " , EndingIndex)

        

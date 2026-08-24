

List=[-2,1,-3,4,-1,2,1,-5,4] #Given List

n=len(List) #Length of List

K=0 #Start of the window at default 

CurrentSum=List[0]
MaxSum=List[0]

for i in range(1,n):# Traversing List 

    if List[i]+CurrentSum > List[i]: # case 1 : 

        CurrentSum=CurrentSum+List[i] # If Case 1 than 

    else: # case 2 or List[i]+CurrentSum < List[i]

        K=i # If this case happens than initialize the window from i .

        CurrentSum=List[i] # If window starts from i sum will also be List[i]


    if CurrentSum>MaxSum: # Check each CurrentSum Calculation to Maxsum to store Maximum

        MaxSum=CurrentSum
        StartingIndex=K
        EndingIndex=i


 # Language Demonstration
print("The Maximum Sum Subarray starts from :" , StartingIndex)
print("Ends At : " , EndingIndex)
print("And The Subarray is : " )

for i in range (StartingIndex , EndingIndex+1): # Print the Subarray

    print( List[i] )
    

print("And Their Sum Is : " , MaxSum)# Print Maxsum.

        



            


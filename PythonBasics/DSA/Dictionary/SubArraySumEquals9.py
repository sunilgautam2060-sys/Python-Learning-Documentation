
#the logic of the problem is calculate  sum value at each i ,
#than calculate required sum :by current prefix sum-target , 
#i will look required value in dictionary if that value exist than i find the subarray
#if not than update the current prefix in dictionary and move on .

#for example my target is to find subarray with sum=9
#i will start traversing the list and calculate sum at each index
#i will compare my current sum and calculate how much is required more ? 
#if my target is 9 than i will keep traversing the list until my sum becomes greater than 9 because 
#my formula to calculate required is: Required=currentPrefixSum-Target, if current sum is smaller than the required will be negative
#so we delibarately try to make the sum greater than target and we try to substract the required value which will equals to target like 
#for currentprefixsum=10 the required will be 1 and we will find 1 in dictionary and fulfill the target.

List=[1,2,3,4,5]

PrefixSum=0
Target=9
Dictionary={} #initializing dictionary.


for i in range(len(List)):

    PrefixSum+=List[i]
    Required=PrefixSum-Target

    if Required in Dictionary:

        StartingIndex=Dictionary[Required]+1
        EndingIndex=i
        print('Subarray Found :')
        print(List[StartingIndex:EndingIndex+1])
        break

    else:
        Dictionary[PrefixSum]=i

    

#Subarray Sum:

#Required Prefix = Current Prefix - Target
        #↓
#Check dictionary
        #↓
#Found → subarray
#Not found → remember current prefix
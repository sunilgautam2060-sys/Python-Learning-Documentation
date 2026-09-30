List = [2, 3, 5, 2, 9, 7, 1] #Given List.

n = len(List) #Size Of List.

SizeOfWindow = 3 #We just need to work with window with size 3 not all possible window.

Sum = 0 #Initializing Sum with 0.

Max = 0 #Initializing Max with 0 ,Normally we initialize with minimum integer value .
#but here we are working with all positive list so we can assume 0 as minimum for now .

# Calculate the first window
for i in range(SizeOfWindow):
    Sum = Sum + List[i] #Accumulating the total sum during 3 iteration.

Max = Sum #Updating the Max with Sum we just calculated . 

SubarrayStartingIndex = 0 # This keeps track of starting index of subarrray.

SubarrayEndingIndex = SizeOfWindow - 1 # This keeps track of Ending index of subarray.

# Slide the window
for i in range(SizeOfWindow, n): # Loops  starts from Remaining window

    Sum = Sum - List[i - SizeOfWindow] + List[i] #Instead of Calculating the sum each time
    #We just add the  value of new element in window and subtract the left most value each time.
    
    
    if Sum > Max: #Is to Put Maximum Sum to Max 
        Max = Sum
        SubarrayStartingIndex = i - SizeOfWindow + 1 # If the new Subarray with Maximum value comes in we should.
        #Track the starting Index .
        
        SubarrayEndingIndex = i #This is for ending index tracking.



#Simple Printing Language Demonstration.
print("Maximum Sum of Subarray is:", Max)
print("The Subarray Starts from:", SubarrayStartingIndex)
print("The Subarray Ends at:", SubarrayEndingIndex)
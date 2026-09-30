
#the core objective is to write the concept of prefix sum in code form , it does not mean
#prefix sum problem will be solve calculating prefix array everytime.

# the core idea of this code is to calculate the prefix sum of the given List or arrays .
# to make prefix array we use simple formula or pattern,
# at first we initialize the prefix[0]=0 ,than start traversing List from index 1.
#at each index i will calculate prefix sum value with formula:
# prefix[i]=prefix[i-1]+List[i-1]



List=[1,2,3,4,5]#given list.

n=len(List) #length of a list.

prefix=[0]*n # this will make the prefix list and initialize with value 0 up to n-1 
             # like: prefix=[0,0,0,0,0...n-1]

for i in range(1,n): #starts traversing from index 1 to n-1.
    prefix[i]=prefix[i-1]+List[i-1] #at each traverse see the previous prefix i.e prefix[i-1] add
                                    #previous list element i.e List[i-1]
                                    #making the formula: prefix[i]=prefix[i-1]+List[i-1].

print(prefix[:n]) #print the prefix sum array .


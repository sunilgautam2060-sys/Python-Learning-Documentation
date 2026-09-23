

#the problem is that we need to merge the given sorted array
#without using extra list or space
#we have 2 list : ListA and ListB
#we extend the ListA equivalent to length of ListB because those element needs to be fit in.

# start pointing the Lists from backside ,the process is:

      #compare the last element of both list,since last element of both list are the largest element .
      #if ListA element is greater than -> put ListA element to the Last index at extended list.
      #if ListB element is greater than ->put ListB element to the Last index at extended list.
      #repeat this step until the condition : i>=0 and j>=0.

    #if the condition fails : there are 2 scenario since the size of ListA and ListB are different 
    # so eventually there will be condition  either one of the list finsh the traversing .
          
           #scenario 1: the ListA completes ->i need to put the remaining ListB element which are already sorted into ListA 
           #scenario 2: the ListB completes ->i need to do nothing since i am extending and merging the list in ListA itself so it is already in right way.
             

ListA=[1,3,5,7,9,20]
m=len(ListA)

ListB=[2,4,6,8,10,17]
n=len(ListB)

ListA.extend([0]*n) #extended the ListA so that i can merge list without extra space.
o=len(ListA)        #now o , will be length of m+n.


i=m-1              #last index pointer to ListA.
j=n-1              #last index pointer to ListB.
k=o-1              #last index pointer to extended ListA ,to merge.

while i>=0 and j>=0: #while this condition satisfies.

    if ListA[i]>ListB[j]: #if ListA element is greater than put into ListA extended.
        ListA[k]=ListA[i]
        k-=1
        i-=1

    else:
        ListA[k]=ListB[j] #if ListB element is greater than put into ListA extended.
        k-=1
        j-=1

while j>=0:               #if the ListB element remains than put it, as it is ,in ListA extended
    ListA[k]=ListB[j]     #here we do not write condition if the ListA element remains ,
    k-=1                  #because we do not need to do anything if ListA element remains ,just put it as it is , and print.
    j-=1            
      
    
#printing output.
print("The Merged Array is : ")
print(ListA)                
     




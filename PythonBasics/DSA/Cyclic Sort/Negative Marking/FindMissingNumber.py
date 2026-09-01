

#the logic of negative indexing to find missing numbers is:
#we traverse the array for each element and mark the index of that element as negative.
#because the index of the element are fixed like index of 1 is 0 ,index of 2 is 1 and so on.
#so if we traverse the array and mark the index of that element as negative than ,   
# the index which is not marked as negative will be the missing number in the array.           

List=[2,4,9,7,8,6]

n=len(List)

i=0
while i<n:
    correct_index=abs(List[i])-1#we take the absolute value of the element.because the element is marked as negative by the element who is already in the array.

    if correct_index<n:           #this will check correct_index is exist in our given array or not. 
                                  #if it is exist than only we will mark it negative.
        List[correct_index]= -List[correct_index]

    i=i+1


#the element who are present in the list will mark their index as negative and the element who are not present in the list will not mark their index as negative.
#so we print the index which is not marked as negative and add 1 to it because the index starts from 0 but the element starts from 1.
print("Missing Numbers are :")
for i in range(n):
    if List[i]>0:
        print(i+1)


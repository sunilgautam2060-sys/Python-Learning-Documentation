

List = [4, 2, 7, 4, 9, 2, 5]

dictionary={}


for i in List:
    if i not in dictionary:
        dictionary[i]=1

    else:
        dictionary[i]+=1



duplicate_element={
k #expression
for k,v in dictionary.items() #traversing
if v>1 #filter
}  
          
print( "The Duplicate Element are:",duplicate_element)




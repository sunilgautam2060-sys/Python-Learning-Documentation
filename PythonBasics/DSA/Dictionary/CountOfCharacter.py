
#basic problem: count how many times each character appears in a string.

string="aabbcaaeefgh"

dictionary={} #Create dictionary.

for character in string:
    if character  not in dictionary: #check key.
        dictionary[character]=1      #if key is not in dictionary than make a key and initialize with value 1.
 
    else:
        dictionary[character]+=1     #if there is already a key , than just increase the existing value by 1. 

print(dictionary)     #print the dictionary.       


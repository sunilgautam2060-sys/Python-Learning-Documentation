

#Problem 2 — Find the first repeated character.

string="programming"
dictionary={}

for character in string:
    if character in dictionary:
        print("The First Repeated Character is:", character)
        break

    else:
        dictionary[character]=1

#Take one character
     #↓
#Is character already a key?
     #↓
#NO → create it with 1
     #↓
#YES → increase its value            
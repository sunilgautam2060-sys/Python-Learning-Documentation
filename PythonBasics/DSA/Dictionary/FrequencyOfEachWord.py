

String = "apple banana apple mango banana apple"
dictionary={}

for word in String.split():
    if word in dictionary:
        dictionary[word]+=1

    else:
        dictionary[word]=1

print(dictionary)            

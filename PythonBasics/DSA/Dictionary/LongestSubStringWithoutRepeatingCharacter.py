


string="abebcdafgabcbad"

left=0

MaxLength=0
dictionary={}

for right in range(len(string)):

    if string[right] not in dictionary:
        dictionary[string[right]]=1

    else:
        dictionary[string[right]]+=1

        while dictionary[string[right]]>1:
            dictionary[string[left]]-=1
            left+=1

    count=right-left+1

    if count>MaxLength:
        MaxLength=count
        start=left
        end=right

print("The Longest Substring Without Repeating Character is : ")
print(string[start:end+1])                    

        
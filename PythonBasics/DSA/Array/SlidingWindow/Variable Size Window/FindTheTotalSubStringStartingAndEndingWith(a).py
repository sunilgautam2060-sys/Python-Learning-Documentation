
#the question say find total subarray which starts and ends with "a"

# in the string "abada" the subarray which starts and ends with "a" are:

# a  , aba  , abada  , a  , ada  , a  .  total =6
#i have to find the total value . 


#we traverse the string with j , 
#  encounter "a" than start "i" from j to n and if encounter "a" than count++
# and print the window from j to i . 


string = "abada"

n = len(string)

j = 0
count = 0

while j < n: #traversing through j .

    if string[j] == "a": #if encounter "a" than start i from j to n .

        for i in range(j, n):

            if string[i] == "a": #if i encounter "a" than count++ because it is a valid subarray which starts and ends with "a".

                count = count + 1 #count the subarray which starts and ends with "a".

    j = j + 1 #j increase .


#print the total count of subarray which starts and ends with "a".
print("Total substrings:", count)


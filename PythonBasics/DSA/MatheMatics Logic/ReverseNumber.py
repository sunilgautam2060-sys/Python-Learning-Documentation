


num=int(input("enter any number "))

reverse=0

while num>0:
    remainder=num%10                 #it will extract last digit.
    reverse=(reverse*10)+remainder   #this will increase place value and add the remainder.
    num=num//10                      #this will floor divide the num by 10.

print("The reverse is : " , reverse)



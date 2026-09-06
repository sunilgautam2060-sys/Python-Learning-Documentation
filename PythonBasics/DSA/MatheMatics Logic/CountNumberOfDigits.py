

num=int(input("enter any number "))

count=0

while num>0:
    num%10       #this will extract last digit.
    count+=1     #this will count .
    num=num//10  #this will decrease place value .

print("The Number Of Digits are:" , count)    


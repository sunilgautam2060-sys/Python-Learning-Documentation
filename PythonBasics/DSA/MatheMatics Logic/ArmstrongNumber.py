

n=int(input("Enter a number "))
temp=n
result=0

count=0

while n>0:
    count+=1
    n=n//10


n=temp
while n>0:
    rem=n%10
    result+=(rem**count)
    n=n//10

if temp==result:
    print("The Number is Armstrong ")  
else:
    print ("The Number is not Armstrong ")

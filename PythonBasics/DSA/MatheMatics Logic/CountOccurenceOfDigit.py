

num=9459949 #we are counting occurence of 9.
count=0

while num>0:
    rem=num%10
    if rem==9:
        count+=1
    num=num//10

print("The Occurence Of Digit 9 is : ", count)    

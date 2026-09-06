

num=343

original=num

reverse=0

while num>0:

    rem=num%10
    reverse=(reverse*10)+rem
    num=num//10

if reverse==original:
    print("The Number is Pallindrome . ")    

else:
    print("The Number is not Pallindrome . ")




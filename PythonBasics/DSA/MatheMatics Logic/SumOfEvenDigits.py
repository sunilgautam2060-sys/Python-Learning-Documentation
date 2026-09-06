
num=6472974

sum=0

while num>0:
    rem=num%10

    if rem%2==0:
        sum+=rem

    num=num//10

print("The Sum Of Even Digits is : ", sum)


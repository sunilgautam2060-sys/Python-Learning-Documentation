

num=int(input("enter any number"))

sum=0

while num>0:
    remainder=num%10    #%10 will returns the ones value from 0 to 9 ,
    sum+=remainder      #sum will keep on accumulating those remainders.  
    num=num//10         #it will floor divide the number by 10.

print("The sum of digits is:" , sum)

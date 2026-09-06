

num=9854711210 #from these number i have to find largest digit i.e 9 .

largest=0

while num>0:
    remainder=num%10           #remainder extract last ones digit .

    if remainder>largest:      #calculating largest so far 
        largest=remainder

    num=num//10                #decreasing the place value of number.

print("The Largest Digit is: " , largest)



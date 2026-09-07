

a=int(input("enter number 1  "))
b=int(input("enter number 2  "))

while b!=0:  
    rem=a%b     #calculate remainder.
    a=b         #put b in a.
    b=rem       #put a%b in b.
#repeat this 3 step algorithm until b, becomes 0. thats the algorithm.


print("GCD of these number is : " , a)


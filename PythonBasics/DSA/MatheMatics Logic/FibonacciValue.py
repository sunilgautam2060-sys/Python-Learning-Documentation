

a=0
b=1

n=int(input("Enter the Value of N :"))

if n==1:
    print("The Fibonacci Value of N is:", a)

elif n==2:
    print("The Fibonacci Value of N is:", b)

else:
    
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c

    print("The Fibonacci Value of N is:", c)
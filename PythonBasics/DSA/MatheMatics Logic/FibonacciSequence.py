


a=0
b=1

n=int(input("Enter The Number Of Fibonacci Sequence You Want "))

for i in range(1,n+1):

    if i==1:
        print(a, end=" ")

    elif i==2:
        print(b, end=" ")

    else:
        c=a+b
        print(c, end=" ")
        a=b
        b=c

        
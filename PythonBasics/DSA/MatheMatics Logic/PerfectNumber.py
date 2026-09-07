

n=int(input("Enter the number "))

result=0


for i in range(1,n//2+1):
    if n%i==0:
        result+=i

if result==n:
    print("It is Perfect Number ")
else:
    print("It is not perfect Number ")


    
    
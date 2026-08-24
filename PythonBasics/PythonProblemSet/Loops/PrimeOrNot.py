
count=0
num=int(input("Enter any Number: "))
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("The Number is Prime ")
else:
    print("The Number is Composite") 

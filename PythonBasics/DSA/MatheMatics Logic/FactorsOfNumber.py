

num=int(input("enter a number "))

bool=False

for i in range(2,num):

    if num%i==0:           

      if bool==False:      #this block is designed to write,The Factors Are: 
         print("The Factors Are: ")
         bool=True

      print(i)

if bool==False:
    print("Number is  Prime it have no factor except 1 and itself  ")


        

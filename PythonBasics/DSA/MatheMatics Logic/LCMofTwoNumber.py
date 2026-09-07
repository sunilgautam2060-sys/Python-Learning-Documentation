

# The Algorithm:
# step1:choose any number between 2 number.
# step2:Take its multiple.
# check whether that multiple is also divisible by the other number. 
# if yes->that's LCM ->stop.
# if no->go to the next multiple.
# repeat.
     
a=int(input("enter a number1 "))
b=int(input("enter a number2 "))

multiple=a

while True:

    if multiple%b==0:
        print("The LCM is : ", multiple)
        break

    multiple+=a
    
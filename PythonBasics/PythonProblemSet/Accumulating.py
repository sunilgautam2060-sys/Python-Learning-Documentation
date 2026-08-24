
#A variable remembers the result from previous iterations and
#gets updated during the next iteration.
#Accumulating Pattern is a mathematical design where a variable is initialized outside the loop.
#The variable gets updated step by step inside the loop ,It stores the value of running result,
#That running result is like memory which later being used by loop variable value and perform different operation like:
#Addition ,Subtraction ,Multiplication, Division anything. 
#An accumulator is a variable that starts with an initial value .
#and is repeatedly updated inside a loop so that it remembers the result built up from previous iterations.



Mylist=[10,20,44,75]
Totalsum=0 #Accumulator Variable
for i in Mylist:
    Totalsum=Totalsum + i
print("Total Sum of List is :" , Totalsum)

#Reverse String
Mystring=input("Enter any Text")
Reversedstring=""#Accumulator Variable
for i in Mystring:
    Reversedstring=i+Reversedstring
print("The Reversed Text is : " , Reversedstring)    


      
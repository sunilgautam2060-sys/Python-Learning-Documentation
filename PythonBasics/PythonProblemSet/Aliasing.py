
#Aliasing in Python happens when you give an object multiple names.
#This means two or more variables point to the exact same location in your computer's memory.
#To clear up this confusion, you only need to remember one golden rule about Python: Variables are labels, not boxes.
#In Python, variables do not hold data; they point to data stored in your computer's memory. 
#When you assign one variable to another (b = a), you are not copying the data. 
#you are just sticking a second label onto the exact same object.
#This is called aliasing
#Whether a variable changes depends entirely on whether the object it points to is mutable.
#(can be changed in place) or immutable (cannot be changed).)


# Case 1: Pointing to the SAME memory block (Aliasing)
list_a = [1, 2, 3]
list_b = list_a  # list_b is an alias
print(list_a is list_b)  # Returns True

# Case 2: Pointing to DIFFERENT memory blocks (Equal values, different locations)
list_c = [1, 2, 3]
list_d = [1, 2, 3]  # A completely new list in memory

print(list_c is list_d)  # Returns False

#The is operator checks for object identity.
#It evaluates to True if two or more variables point to the exact same memory block (the same address), and False if they do not
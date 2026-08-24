#Mutability means that the value of an object can be changed .
# after it has been created. 
# In Python, some objects are mutable, while others are immutable. 
# for example, lists and dictionaries are mutable, while strings and tuples are immutable.

fruits=["apple", "banana", "cherry"]
fruits[0]="kiwi" #changing the value of first element of list
print(fruits) #Output: ['kiwi', 'banana', 'cherry'] 
fruits[1:3]=["orange", "grape"] #mutate a list with slice operator
print(fruits) #Output: ['kiwi', 'orange', 'grape']


# Lets see an example of immutable object i.e. tuple
my_tuple=("apple", "banana", "cherry")
my_tuple[0]="kiwi" #This will raise an error because tuples are immutable
print(my_tuple) #Output: TypeError: 'tuple' object does not support item assignment




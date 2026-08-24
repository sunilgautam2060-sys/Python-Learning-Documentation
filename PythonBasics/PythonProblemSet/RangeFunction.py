# range includes start value but excludes end value like slice operator.
#range(5) will print 0,1,2,3,4 
print("The numbers from range(5) are : ")
for i in range(5):
    print(i)

#I want to print those numbers in list so use list() and pass range() as an argument.
numbers = list(range(5))
print("The numbers from list(range(5)) are : ")
print(numbers)

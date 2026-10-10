

def print_triangle(row,column=0):
    #this is base-case for recursion.
    if row==0:
        return
    if column<row:
        print_triangle(row,column+1) #this function task is to print *.
        print("*",end="")
    else:
        print_triangle(row-1,0) #this function task is to print new line.
        print("")#this is for new line.

print_triangle(5)
print("")
print(" ")

def print_triangle_reverse(row,column=0):
    if row==0:
        return
    if column<row:
        print("*",end="")
        print_triangle_reverse(row,column+1) #this function task is to print *.
    else:
        print("")#this is for new line.
        print_triangle_reverse(row-1,0) #this function task is to print new line.


print_triangle_reverse(5)

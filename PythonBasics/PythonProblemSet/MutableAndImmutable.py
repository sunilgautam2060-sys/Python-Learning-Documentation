#Methods in Python are classified based on whether ,
#they change the original object in place(mutating) or leave
#the original object alone and return a brand new object instead(non-mutating)

#Mutating Methods
#list.append()
#list.pop()
#list.sort()

#Non-Mutating Methods
#string.upper()
#string.lower()
#list.index()

string="Hello , Sunil"
x=string[2]*4
print(x)
SlicedString=string[0:10]#this will not change original string
IndexString=string.index(",")#this will not change original string
print(string)
print(string +  "cat")#concatinating string 
print(string)#still no change in original string


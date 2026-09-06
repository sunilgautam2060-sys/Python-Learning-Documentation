

string="968-Maria, ( D@t@ Engineer );; 27y  "
#make it: 
#name: maria | role: data engineer | age: 27

#data cleaning. 
string=string.replace('@' , 'a' )
string=string.replace('968-' , '')
string=string.replace('(','')
string=string.replace(')','')
string=string.replace(';','')
string=string.lstrip()
string=string.replace('y','')
string=string.replace(',','')
string=string.lower()

#split data
Words=string.split()
#Words=['maria' 'data engineer' '27']
print("name:" ,Words[0], "| role:",Words[1] , "| age:", Words[2] )


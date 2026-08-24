

#Short string split
string1="I Love Mathematics"
split_string1=string1.split("e")
print(split_string1)


#Let's go towards joining 
ColorList=["red","blue","orange","pink"]
MoodTuple=("sad","angry","happy","confident")
glue="/"
glue1=";"
JoinnedList=glue1.join(ColorList)
JoinnedTuple=glue.join(MoodTuple)
print(JoinnedList)
print(JoinnedTuple)

#Let's join without variables
print("**".join(ColorList))

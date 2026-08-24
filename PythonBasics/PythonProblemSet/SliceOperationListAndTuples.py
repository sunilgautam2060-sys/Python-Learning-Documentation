#Basic Tuple as well as Slice Operation Demonstration

MyPersonalTuples=("listenToYourShadow" , "TalkToYourself" , "DoBoringTaskForcefully" , "ImproveFocus" , "TryToWorkUncomfortably")
print("The Size of MyPersonalTuples is : " , len(MyPersonalTuples))

#This slice operation will print the elements from index 1 to 3(4 is excluded)
print(MyPersonalTuples[1:4])

print("Tuples with the gap of 2 elements are :" )

#This slice operation will print every second element from the tuple like index 0,2,4
print(MyPersonalTuples[::2])

print("Let's Move Towards List Now")

MyPersonalList=["LimitScreenTime" , "ObserveYourself" , "BreatheAndLiveCalm" , "NoticeEverything" , "DoProgrammingStuff" , "LimitPressureEnjoyEverything"]
print( "The Length of MyPersonalList is :" , len(MyPersonalList))

#This slice operation will print the elements from index 2 to 4(5 is excluded)
print(MyPersonalList[2:5])
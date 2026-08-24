#Ask the user for their name and birth year,
#  then print a sentence stating their approximate age.
name=input("Enter your name ")
BirthYear=int(input("Enter your BirthYear"))
CurrentYear=2026
Age=CurrentYear-BirthYear
print("Your age might be : ", Age)

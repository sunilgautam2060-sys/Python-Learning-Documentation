import random

RandomNumber = random.randint(1, 7)

UserNumber = int(input("Enter the Number You Want: "))

NumberOfTimes = int(input("Enter the Number of times you want to play the game: "))

CheckIn = False

for i in range(NumberOfTimes):

    if UserNumber == RandomNumber:

        CheckIn = True

        print("Congratulations! You Successfully guessed the number at Attempt {}".format(i + 1))

        break

    elif UserNumber > RandomNumber:

        print("Your Guess is Slightly Higher")

    else:

        print("Your Guess is Slightly Lower")

    if i < NumberOfTimes - 1:
        UserNumber = int(input("Enter The Number Again. It is your {} Attempt: ".format(i + 2)))


if CheckIn == False:
    print("Sorry, Time is Over. You can try another time.")
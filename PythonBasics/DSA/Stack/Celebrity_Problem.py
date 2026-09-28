
#Celebrity knows nobody but,everybody will know celebrity .
#Look at matrix[2] it knows  nobody , but every other index knows matrix[2].
#so 2 is the celebrity here .


class Solution:

    def celebrity_problem(self):

        # 1 means Person A knows Person B
        # 0 means Person A does not know Person B

        Matrix = [
            [0, 0, 1, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 0]
        ]

        Stack = []

        # Put every person's index into the stack
        for Person in range(len(Matrix)):
            Stack.append(Person)

        # Eliminate people who cannot be the celebrity
        while len(Stack) > 1:

            PersonA = Stack.pop()
            PersonB = Stack.pop()

            # If A knows B:
            # A cannot be the celebrity because a celebrity knows nobody.
            # So B remains as the possible candidate.
            if Matrix[PersonA][PersonB] == 1:
                Stack.append(PersonB)

            # If A does not know B:
            # B cannot be the celebrity because everybody must know
            # the celebrity.
            else:
                Stack.append(PersonA)

        # Only one possible candidate remains
        PossibleCelebrity = Stack.pop()

        # Verify the candidate
        for Person in range(len(Matrix)):

            if Person == PossibleCelebrity:
                continue

            # Celebrity must know nobody
            if Matrix[PossibleCelebrity][Person] == 1:
                print("There is no celebrity")
                return

            # Everybody must know the celebrity
            if Matrix[Person][PossibleCelebrity] == 0:
                print("There is no celebrity")
                return

        print(PossibleCelebrity, "is the celebrity")


SolutionObject = Solution()
SolutionObject.celebrity_problem()
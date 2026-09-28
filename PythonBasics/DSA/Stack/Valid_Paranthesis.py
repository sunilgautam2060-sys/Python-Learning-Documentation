


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        # Go through every bracket
        for bracket in s:

            # Opening bracket → push into stack
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)

            else:

                # Closing bracket but nothing to match
                if len(stack) == 0:
                    return False

                # Take the most recent opening bracket
                ch = stack.pop()

                # Check whether the brackets match
                if (bracket == ")" and ch == "(") or \
                   (bracket == "]" and ch == "[") or \
                   (bracket == "}" and ch == "{"):

                    continue

                else:
                    return False

        # If nothing is left, all brackets were matched
        if len(stack) == 0:
            return True
        else:
            return False


s=Solution() 
print(s.isValid(["(","[","{","}","]",")"]))  





class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack1 = []
        stack2 = []

        # Process first string
        for i in s:

            if i != '#':
                stack1.append(i)

            else:
                if stack1:
                    stack1.pop()

        # Process second string
        for j in t:

            if j != '#':
                stack2.append(j)

            else:
                if stack2:
                    stack2.pop()

        # Compare the final strings
        return stack1 == stack2

s=Solution()
print(s.backspaceCompare("ab#c", "ad#c"))  # Output: True       
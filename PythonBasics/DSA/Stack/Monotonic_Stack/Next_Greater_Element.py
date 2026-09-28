  

#previous greater/smaller=iterate from left to right.
#next greater/smaller=iterate from right to left.


class Solution:

    def Next_Greater_Element(self):

        nums = [19, 2, 4, 9, 3, 5, 8, 10]

        ans = [-1] * len(nums)

        stack = []

        # Start from the right side
        for i in range(len(nums) - 1, -1, -1):

            # Remove elements that are smaller
            # because they cannot be the answer
            while len(stack) > 0 and stack[-1] <= nums[i]:
                stack.pop()

            # The top of stack is now
            # the next greater element
            if len(stack) > 0:
                ans[i] = stack[-1]

            # Put current element into stack
            stack.append(nums[i])

        return ans


s = Solution()
print(s.Next_Greater_Element())

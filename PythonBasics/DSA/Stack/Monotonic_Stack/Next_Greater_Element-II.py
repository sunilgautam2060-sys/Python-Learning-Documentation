


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:

        n = len(nums)
        ans = [-1] * n
        stack = []

        # Go through array twice because it is circular
        for i in range(2 * n - 1, -1, -1):

            CurrentIndex = i % n

            # Remove elements that cannot be greater
            while len(stack) > 0 and stack[-1] <= nums[CurrentIndex]:
                stack.pop()

            # Only fill answer for original array
            if i < n and len(stack) > 0:
                ans[CurrentIndex] = stack[-1]

            stack.append(nums[CurrentIndex])

        return ans


s = Solution()
print(s.nextGreaterElements([1, 2, 1]))


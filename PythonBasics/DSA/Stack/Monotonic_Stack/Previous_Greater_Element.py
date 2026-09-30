
#previous greater/smaller=iterate from left to right.
#next greater/smaller=iterate from right to left.

#the core logic is:
#visit each nums[i] : two possible scenario 
#either stack is empty : just append nums[i] to stack and move on ,do not do
#anything in (ans[]) because empty stack means there is no greater previous element so.

#or stack is not empty : than pop()  until stack[-1] is smaller element
#  than nums[i] ,if big number comes in (ans[]) will get updated by that number.
#during the poping() until stack[-1] is smaller element we may make the stack empty ,
#its fine if stack is empty we can tell there is no greater number than nums[i] so do not 
#do anything to the ans[].



class Solution:

    def Previous_Greater_Element(self):

        nums=[19, 2, 4, 9, 3, 5, 8, 10]
        n=len(nums)

        ans=[-1]*n
        
        stack=[]

        for i in range(n):


            #keep poping() until stack[-1]<nums[i] .
            #two possible scenario:len(stack) will be empty.
            #scenario 2:len(Stack won't be empty)
            while len(stack)!=0 and stack[-1]<nums[i]:
                stack.pop()


            #if len(Stack) is not empty only than.
            if len(stack)!=0:
                ans[i]=stack[-1]

            #this operation is fundamental for each scenario.
            stack.append(nums[i])


        return ans

s=Solution()
print(s.Previous_Greater_Element())       
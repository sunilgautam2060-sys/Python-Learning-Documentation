

class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack=[]
        
        for ch in s:
            if len(stack)==0 or stack[-1]!=ch:
                stack.append(ch)
                

            else :
             stack.pop()
             

        result=""
        while len(stack)!=0:
            result=stack.pop()+result


        return result

s=Solution()
print(s.removeDuplicates("abbaca"))   
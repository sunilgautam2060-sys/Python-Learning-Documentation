

#the logic is same as pivot index firstly we calculate total sum or product
# than traverse each index and calculate left and right sum/product 
#leftproduct=left side product up to index i-1 means if we are at index 5 leftproduct will be ,
#product of element from index0 to index4.
#Rightproduct=totalproduct/leftproduct/currentindexvalue.



class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        answer=[]

        left_product=1
        right_product=1
       
        
        #left to right traversal to calculate left product.
        for i in range(len(nums)):
            answer.append(left_product)
            left_product*=nums[i]

     
        #right to left traversal to calculate right product.

        for i in range(len(nums)-1,-1,-1):
            answer[i]*=right_product
            right_product*=nums[i]

        return answer        

s=Solution()
print(s.productExceptSelf([1,2,3,4,5])  )



        
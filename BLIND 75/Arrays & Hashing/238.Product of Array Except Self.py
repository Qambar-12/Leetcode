class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        #Moving in two passes (loops) from one in forward direction and other in backward direction computing product of prefix and postfix for each element in nums array
        prefix,postfix = 1 , 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        for j in range(len(nums)-1,-1,-1):
            res[j] *= postfix
            postfix *= nums[j]
        return res        

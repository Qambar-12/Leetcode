class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        #binary search problem with search space/range ---> [min(nums) , max(nums)]
        #defining a helper function for valid capability i.e traversing and determing that there are atleast k houses <= capabilty 
        #while also considering capability condition
        def is_valid(capability):
            count = 0
            i = 0
            while i < len(nums):
                if capability >= nums[i]:
                    i += 2
                    count += 1
                else:
                    i += 1
                #because we only need k for capability to be valid    
                if count == k:
                    break        
            return count == k        
        l , r = min(nums) , max(nums)
        res = 0
        while l <= r:
            m = (l+r)//2 
            if is_valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res                
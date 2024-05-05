class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #there is guaranteed to be a duplicate b/c len(nums) == n + 1 and 1 <= nums[i] <= n
        #Binary search range is from 1 to n
        #O(nlogn) time complexity
        #and O(1) space complexity
        l , r = 1 , len(nums)-1
        ans = 0
        while l <= r:
            #prevent overflow because it minimizes the size of intermediate values involved in the calculation.
            #i.e evaluates (r-l) results im a smaller intermediate value first
            mid = l + ((r-l)//2)
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count <= mid :
                l = mid + 1
            else:
                #b/c mid can possibly be an answer
                ans = mid
                r = mid - 1
        return ans                  

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #Two pointer solution / Sliding window technique
        #edge test case
        if k == 1:
            return 0
        else:
            diff = 10**5
            nums.sort()
            i ,j = 0,k
            while j <= len(nums):
                d = nums[j-1] - nums[i]
                if d < diff:
                    diff = d
                i += 1
                j += 1    
            return diff    

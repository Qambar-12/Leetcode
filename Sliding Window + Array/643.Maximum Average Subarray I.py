class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        total = maximum = sum(nums[:k])
        for r in range(k,len(nums)):
            total += nums[r] - nums[l]
            maximum = max(maximum,total)
            l += 1
        return maximum/k        

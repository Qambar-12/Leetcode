class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        #if we translate the problem to aim that we need to find max-size of a window such that it's sum is equal to sum(nums) - X = targert
        #then the max-size of this window means min opearations from edges of array that total upto X
        target = sum(nums) - x
        max_window = -1
        curr_sum = 0
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while l <= r and curr_sum > target:
                curr_sum -= nums[l]
                l += 1
            if curr_sum == target:
                max_window = max(max_window, r - l + 1)    
        return -1 if max_window == -1 else (len(nums) - max_window )        

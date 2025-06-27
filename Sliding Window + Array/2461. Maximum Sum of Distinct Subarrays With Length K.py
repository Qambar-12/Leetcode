class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #conventional sliding window solution
        l = 0
        visited = {}
        res,currSum = 0 , 0
        for r in range(len(nums)):
            currSum += nums[r]
            if nums[r] in visited:
                visited[nums[r]] += 1
            else:
                visited[nums[r]] = 1    
            if r-l+1 > k:
                currSum -= nums[l]
                if nums[l] in visited:
                    visited[nums[l]] -= 1
                    if visited[nums[l]] == 0:
                        del visited[nums[l]]
                l += 1
            if r-l+1 == k:
                if len(visited) == k:
                    res = max(res,currSum)         
        return res
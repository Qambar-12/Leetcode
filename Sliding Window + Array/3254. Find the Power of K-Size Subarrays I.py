class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        #sliding window problem 
        res = []
        l = 0
        #consecutive count cannot be less than one i.e a single element
        consecutive_count = 1
        for r in range(len(nums)):
            if r > 0 and nums[r-1]+1 == nums[r]:
                consecutive_count += 1
            if r - l + 1 > k:
                if nums[l+1] == nums[l]+1:
                    consecutive_count -= 1
                l+=1
            if r-l+1 == k:
                if consecutive_count == k:
                    res.append(nums[r])
                else:
                    res.append(-1)        
        return res
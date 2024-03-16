class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #sorting operation makes the overall time complexity O(nlogn)
        nums.sort()
        #Sliding window technique implemented using two pointers
        i , j = 0 , 0
        #total is the running total of window elements
        res , total = 0 ,0
        while j < len(nums):
            total += nums[j]
            #We are trying to make nums[j] as the most freq element
            #so the loop continues until the size of window is invalid i.e we cannot make all elements in our window to nums[j] by performing k operations
            while nums[j]*(j-i+1) > total + k:
                total -= nums[i] 
                i += 1
            #size of window = j - i + 1 b/c index starts from 0
            res = max(res,j-i+1)
            j += 1
        return res        

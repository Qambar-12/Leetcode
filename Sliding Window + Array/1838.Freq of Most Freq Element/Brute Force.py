def maxFrequency(nums, k):
    if all(n == nums[0] for n in nums) :
            return len(nums)
    else:        
        nums.sort(reverse = True)
        i , j = 0 , 0
        res = 0
        while i <= len(nums)-2:
            freq,op = 0,k
            while op > 0 and j < len(nums):
                if nums[i] - nums[j] <= op:
                    op -= nums[i] - nums[j]
                    freq += 1
                    j += 1
                else:
                    break 
            i += 1  
            j = i    
            res = max(res,freq)            
        return res        

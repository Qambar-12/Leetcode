class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or k==0 or len(nums) == len(set(nums)) :
            return False
        i,j =0,1
        #Sliding window approach (Two-pointers)
        while i <= len(nums)-2  :
            if j <= len(nums)-1:
                if (nums[i] == nums[j]) and abs(i-j) <= k:
                    return True
                else:
                    #expanding size of window when max size is not reached
                    if abs(i-j) < k :
                        j += 1
                    else:
                        #when max size is reached shrinking back the size of window
                        i += 1
                        j = i + 1
            else:
                i+= 1
                j = i + 1        
        return False

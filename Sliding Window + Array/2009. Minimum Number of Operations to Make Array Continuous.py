class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #for nums to be continuos all elements must be consecutive and unique
        #the order of nums doesnot matter and we can sort it to our advantage
        #idea is for every element x in nums  we can look for range [x, x+n-1]
        #and where the changes needed to be made looking at hashmap are min return it as res
        #The above approach is O(n^2)

        #we can optimize it by sliding window technique
        #sorting is O(nlogn)
        length = len(nums)
        res = length     #the max operations in worst case
        #for removing duplicate we use hashset and it works because although we remove duplicate we use original lenght of nums for calc
        nums = sorted(set(nums))
        #this time we want to implement for each left pointer and right keeps on expanding
        r = 0
        for l in range(len(nums)):
            #we want our right pointer to stop atleast one past the range so we donot include -1
            while r < len(nums) and nums[r] < nums[l] + length:
                r += 1
            window = r-l   #doesnot include +1 because we already would stop after the actual range
            res = min(res , length - window)    
        return res    
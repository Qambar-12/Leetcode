class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #three pointer sliding window technique (L , M , R)
        #continue expanding window right pointer until exactly k odd no.
        #check if window size is valid
        #then shift the middle pointer to first odd occurence 
        #and tot nice subarray in b/w are M-L+1

        res , oddCount = 0 , 0
        l , m = 0 , 0
        for r in range(len(nums)):
            #check if number is odd first
            if nums[r] % 2:
                oddCount += 1
            #check the window size 
            while oddCount > k:
                if nums[l] % 2:
                    oddCount -= 1
                l += 1
                #reset the middle pointer
                m = l
            #if oddCount == k:
            if oddCount == k:
                #continue till first odd occurence
                while not nums[m] %2:
                    m += 1
                res += (m - l ) + 1   
        return res    
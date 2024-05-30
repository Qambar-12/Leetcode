class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #using sliding window approach is not possible because nums[i] can be negative
        #so incrementing our right pointer doesnot guarantee that we are increasing window size
        #and so is case while decrementing pointer doesnot guarantee that we are decreasing window size
        

        #using a hashmap storing prefix-sum at every point {prefixSum : count}
        #for every integer we subtract its prefixSum - k and check whether this prefix sum already exists in hashmap
        #i.e are there some elements subarray that can chopped off from current array to get sum as k
        #base case is {0 : 1} i.e zero if we get zero as result for prefixSum - k then it means that there subarray till this point is a valid seq that sums upto k and we donot need to chop off anything
        res , currPrefixSum = 0 , 0
        prefixSum = {0:1}
        for n in nums:
            currPrefixSum += n
            diff = currPrefixSum - k
            if diff in prefixSum :
                res += prefixSum[diff]
            if currPrefixSum in prefixSum:
                prefixSum[currPrefixSum] += 1
            else:
                prefixSum[currPrefixSum] = 1    

        return res 

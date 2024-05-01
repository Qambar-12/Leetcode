class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Time complexity O(n)      Space complexity O(1)
        nums = set(nums)        #Lookup using in operator is O(1) solution
        smallest_pos_missing = 1
        while smallest_pos_missing in nums:
            smallest_pos_missing += 1
        return smallest_pos_missing            

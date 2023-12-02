class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Since sets donot allow duplicate elements
        if len(set(nums)) != len(nums):
            return True
        else:
            return False    

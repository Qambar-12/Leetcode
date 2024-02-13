class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        numsSet = set(nums)
        for num in numsSet:
            res = nums.count(num)
            if res > (n/2):
                return num

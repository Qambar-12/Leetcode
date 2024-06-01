class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #combinations aspect because order is not important and repetion is not allowed
        res = 0
        count = collections.Counter(nums)
        for i in count.keys():
            if count[i] >= 2:
                res += ((factorial(count[i]))/(factorial(2)*factorial(count[i]-2)))
        return int(res)

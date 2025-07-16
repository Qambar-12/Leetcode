class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        #The maximum number of balls can never be greater than max(nums)
        #thus the search range is [1,max(nums)]
        #BINARY SEARCH
        #for every element in search range we need to validate whether the bag can be divided into these many balls within maxOperations

        def can_split(max_balls):
            ops = 0
            for n in nums:
                ops += (math.ceil(n/max_balls) -1)
                if ops > maxOperations:
                    return False
            return True

        l , r = 1 , max(nums)
        while l < r:
            m = l+(r-l)//2    
            if can_split(m):
                r = m
            else:
                l = m+1
        return l                
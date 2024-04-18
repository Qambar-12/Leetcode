class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        #Binary range search range
        l,r = 1 , max(piles)
        #initializing with max possible value
        res = r
        while l <= r:
            mid = (l+r)//2
            hours = 0
            for p in piles:
                hours += ceil(p/mid)  
            if hours <= h:
                r = mid - 1
                res = min(res,mid)  
            else:
                l = mid + 1                   
        return res    
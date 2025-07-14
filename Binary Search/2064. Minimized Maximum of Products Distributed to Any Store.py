class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        #not every store must be allocated product 
        #but every product must be allocated to some store
        #The min any store can receive is 0
        #The max any store can receive is max(quantities)
        #This becomes a BINARY SEARCH prob where search range is 0 to max(quantities)
        #For every x we need to check that can it be distributed i.e stores <= n

        #helper function
        def can_distribute(x):
            stores = 0
            for q in quantities:
                stores += math.ceil(q/x)
            return stores <= n

        #binary search
        res = 0
        l , r = 1 , max(quantities)
        while l <= r:
            x = (l+r)//2 #to prevent overflow l+(r-l)//2
            if can_distribute(x):
                res = x
                r = x-1
            else:
                l = x+1
        return res                    
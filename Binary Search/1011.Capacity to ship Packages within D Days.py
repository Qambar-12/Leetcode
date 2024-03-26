class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #left and right pointers are lower and upper bounds respectively for binary search
        #Because ship must atleast have capacity equal to max of weights and atmost capacity must be sum of all weights
        #So we need to perform binary search in this space
        l,r = max(weights),sum(weights)
        #result is initialized with a maximum i.e sum of all weights
        res = r

        def canShip(cap):
            #initializing ships to 1 because we would atleast need 1
            ships = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    #currCap for new ship re-assigning
                    currCap = cap
                currCap -= w
            return ships <= days

        #Binary search algorithm for capacity (while pointers have not crossed eachother)
        while l <= r:
            #finding mid this way may result in overflow sometimes
            cap = (l+r)//2
            #if true we need to find a more min capacity by reducing our search space
            if canShip(cap):
                res = min(res,cap)
                r = cap - 1
            else:
                l = cap + 1

        return res            



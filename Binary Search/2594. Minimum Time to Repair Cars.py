class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        #min time it would take is atleast one min
        #and max time it would take is max(ranks)*cars^2 i.e the slowest mechanic repairing all cars alone
        #this gives rise to a search space and hence binary search problem

        #for each time that we get in the range we need to check for cars
        #i.e n = sqrt(time/rank) gives how many cars can that particular mechanic with a rank repair
        #and sum them up for all cars 
        #if the sum at any point is greater than int cars then we need to search to left of mid pointer
        from math import sqrt
        def can_repair_cars_in_time(time):
            tot = 0
            for r in ranks:
                c = int(sqrt(time/r))
                tot += c
                if tot >= cars:
                    return True
            return tot >= cars         
        l , r = 1 , max(ranks)*cars*cars
        res = -1 
        while l <= r:
            time = (l+r)//2
            if can_repair_cars_in_time(time):
                res = time
                r = time - 1
            else:
                l = time + 1
        return res           
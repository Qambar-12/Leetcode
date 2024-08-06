class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        #first of all we need to sort the integer array because we need to compare adjacent elements
        #for pair diff to be minimum
        #our return value would be some where in b/w 0 <= nums[i] <= 10^9
        #so we can run a greedy binary algorithm here with time complexity O(nlogm) = O(9n) = O(n)
        nums.sort()
        #for the binary search values that we pick (as return values) we run a greedy algorithm everytime
        #to satisfy that we must have p pairs that each whose diff <= choosen binary val (b/c our val is max of min)
        #as soon as our condition is satisfied we return

        #Edge test case if p = 0
        if p == 0:
            return 0
        def isValid(searchVal):
            #greedy algorithm part (helper function)
            i,count = 0, 0
            #to avoid index out of range error
            while i < len(nums)-1:
                if abs(nums[i]-nums[i+1]) <= searchVal:
                    count += 1
                    i += 2          #b/c we cannot an index two times
                else:
                    i += 1
                if count == p:
                    return True
            return False                

        l , r = 0 , 10**9
        res = 10**9
        while l <= r:
            m = (l+r)//2
            #finding even more smaller value if we have found one
            if isValid(m):
                res = m
                r = m - 1
            #look for a larger value that satisfies
            else:
                l = m + 1    
        return res        

                

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #with memoization to reduce the time complexity from O(2^n) to O(n)
        memo = {}
        #recurrecne relation : cost to reach ith step is 
        #cost of current step i + min(min(i+1)  , min(i+2))
        def minCost(i):
            #base case 
            if i >= len(cost):
                return 0
            if i not in memo:
                memo[i] = cost[i] + min(minCost(i+1),minCost(i+2))
            return memo[i]
        return min(minCost(0),minCost(1))            

class Solution:
    #Memoization is an optimization technique used to improve the performance of recursive algorithms. It involves storing the results of expensive function calls and reusing them when the same inputs occur again. Memoization reduces redundant calculations by keeping a "memory" (usually a dictionary or array) of previously computed results.
    def rob(self, nums: List[int]) -> int:
        # Define a helper function with memoization
        def rob_helper(house):
            # Base cases
            if house >= len(nums):
                return 0
            
            # If result is already computed, return it
            if house in memo:
                return memo[house]
            
            # Recurrence relation
            # Option 1: Rob the current house and move to index + 2
            # Option 2: Skip the current house and move to index + 1
            memo[house] = max(nums[house] + rob_helper(house + 2), rob_helper(house + 1))
            return memo[house]
        
        # Edge case: No houses
        if not nums:
            return 0
        
        # Initialize memoization dictionary
        memo = {}
        return rob_helper(0)
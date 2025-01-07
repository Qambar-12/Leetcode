class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # #Dynamic Programming (Bottom-up approach i.e we compute amounts from 0 to amount)
        # #Iterative version      ----> BOTTOM-UP-APPROACH
        # #DP array (we initialize all values with max initially)
        # dp = [amount+1]*(amount+1)
        # #base case (assumed)
        # #e.g amount = 7     , coins = [1,3,4,5]
        # #dp[0] = 0
        # #dp[1] = 1
        # #dp[2] =  min(dp[2], 1 + dp[2-1])  (breaks for values when it becomes negative)
        # #dp[3] =  min(dp[3] , 1 + dp[3-1])
        # #dp[3] =  min(dp[3] , 1 + dp[3-3])   (breaks for values when it becomes negatives)
        # #dp[4] =  min(dp[4] , 1 + dp[4-1])
        # #dp[4] =  min(dp[4] , 1 + dp[4-3])
        # #dp[4] =  min(dp[4] , 1 + dp[4-4])   (breaks for values when it becomes negatives)
        # #dp[5] = min(dp[5] , 1 + dp[5-1])
        # #dp[5] = min(dp[5] , 1 + dp[5-3])
        # #dp[5] = min(dp[5] , 1 + dp[5-3])
        # #dp[5] = min(dp[5] , 1 + dp[5-4])
        # #dp[5] = min(dp[5] , 1 + dp[5-5])


        # dp[0] = 0
        # for a in range(1,amount+1):
        #     for c in coins:
        #         if a-c >= 0:
        #             dp[a] = min(dp[a], 1 + dp[a-c] )
        #         # else:
        #         #     break    (only when list is sorted)
        # #we need to return -1 if intial value remains            
        # return dp[amount] if dp[amount] != amount+1 else -1  

        #Recursive sol with memoization (TOP-DOWN APPROACH)
        memo = {}
        def dfs(amount):
            #base case 
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins       


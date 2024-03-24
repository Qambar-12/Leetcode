class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #l = buy , r = sell (pointers of window)
        l,r = 0,1
        maxP = 0
        while r < len(prices):
            #maximum profit is calculated when buy is less than sell
            #The l variable (buy) is not updated until buy is greater than sell
            if prices[l] < prices[r] :
                maxP = max(maxP,(prices[r]-prices[l]))
            else:
                l = r
            #The size of window continues to increase from right
            r += 1
        return maxP            

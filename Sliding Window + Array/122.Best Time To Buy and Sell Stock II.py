class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(set(prices)) == 1 or prices == sorted(prices,reverse=True):
            return 0
        elif prices == sorted(prices) :
            return prices[-1] - prices[0] 
        else:
            maxProfit = 0
            for i in range(1,len(prices)):
                if prices[i] > prices[i-1]:
                    maxProfit += (prices[i]-prices[i-1])
            return maxProfit         

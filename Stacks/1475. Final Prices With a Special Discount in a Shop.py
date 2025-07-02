class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #monotonic increasing stack problem
        res = [p for p in prices]
        stack = []      #holds indexes , always stores if in increasing order
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]    
            stack.append(i)  
        return res    
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #sliding window sol
        l = 0
        alreadySatisfied = 0
        windowScore, max_window = 0 , 0
        for r in range(len(customers)):
            if grumpy[r] == 1:
                windowScore += customers[r]
            else:
                alreadySatisfied += customers[r]

            if r-l+1 > minutes:
                if grumpy[l] == 1:
                    windowScore -= customers[l]
                l += 1

            max_window = max(max_window,windowScore)
        return alreadySatisfied + max_window                    
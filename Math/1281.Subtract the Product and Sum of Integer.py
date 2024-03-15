class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum,prod = 0 , 1
        while n > 0 :
            rem = n % 10
            Sum += rem
            prod *= rem
            n = n//10
        res = prod - Sum
        return res    

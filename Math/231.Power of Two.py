class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i,prod = 0,1
        while prod<=n:
            prod = 2**i
            i += 1
            if prod == n:
                return True
        return False       

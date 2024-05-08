class Solution:
    def fib(self, n: int) -> int:
        # Base cases: F(0) = 0 and F(1) = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # Recursive case: F(n) = F(n - 1) + F(n - 2)
        else:
            return self.fib(n - 1) + self.fib(n - 2)   
        return self.fib(n)        

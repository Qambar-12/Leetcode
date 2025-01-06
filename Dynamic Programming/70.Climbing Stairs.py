class Solution:
    def climbStairs(self, n: int) -> int:
        #WITHOUT MEMOIZATION O(2^n)
        # if n == 1: 
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     #recurrence relation :
        #     #1.either take 1 step and then n-1 steps remaining 
        #     #2.OR 2 step and then n-2 steps remaining
        #     return self.climbStairs(n-1)+self.climbStairs(n-2)

        #WITH MEMOIZATION
        # memo = {}
        # def climb(n):
        #     if n <= 2:
        #         return n
        #     if n not in memo:
        #         memo[n] = climb(n-1) + climb(n-2)
        #     return memo[n]
        # return climb(n)            

        #Iterative version similar to Fibonacci series
        # array = [1,2]
        # for i in range(2,n+1):
        #     array.append(array[i-1]+array[i-2])
        # return array[n-1]    

        #Iterative version space optimized
        a , b = 1 , 2
        for i in range(n-1):
            a , b = b , a+b
        return a    
           

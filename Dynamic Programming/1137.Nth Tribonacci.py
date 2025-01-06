class Solution:
    def tribonacci(self, n: int) -> int:
        #memoization O(n)  --> recursive version
        # memo = {}
        # def dfs(n):
        #     #base cases
        #     if n == 0: 
        #         return 0
        #     elif n == 1 or n == 2:
        #         return 1
        #     else:
        #         if n not in memo:
        #             memo[n] = dfs(n-3) + dfs(n-2) + dfs(n-1)
        #         return memo[n]   
        # return dfs(n)             

        #Iterative Version 1
        # array = [0,1,1]
        # for i in range(3,n+1):
        #     array.append(array[i-3]+array[i-2]+array[i-1])
        # return array[n]

        #Iterative version 2
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            a , b , c = 0 , 1 ,1 
            for i in range(n-2):
                a , b , c = b , c , a+b+c
            return c    


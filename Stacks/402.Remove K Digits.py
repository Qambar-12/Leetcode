class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while stack and k and stack[-1] > d:
                k -= 1
                stack.pop()
            #to prevent leading zeroes
            if stack or d != '0':
                stack.append(d)    
        #i.e for e.g when digits in strings arranged in ascending order
        #if k is still greater than zero
        if k:
            stack = stack[:-k]
        
        return "".join(stack) or '0' 

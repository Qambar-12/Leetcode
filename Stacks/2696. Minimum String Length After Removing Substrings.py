class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for ch in s :
            if stack:
                if (ch == 'B' and  stack[-1] == 'A') or (ch == 'D' and  stack[-1] == 'C') :
                    stack.pop()
                else:
                    stack.append(ch)    
            else:
                stack.append(ch)      
        return len(stack)            
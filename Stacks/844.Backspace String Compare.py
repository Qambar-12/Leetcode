class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            x = len(s)
        else:
            x = len(t)    
        stack1, stack2 = [] , []
        for ch in range(x):
            if ch <= len(s)-1:
                if s[ch] != '#':
                    stack1.append(s[ch])
                else:
                    if stack1:
                        stack1.pop()  
            if ch <= len(t)-1 :
                if t[ch] != '#':
                    stack2.append(t[ch])
                else:
                    if stack2:
                        stack2.pop()   
            
        return stack1 == stack2    

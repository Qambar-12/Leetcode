class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #using stack data structure
        #for every opening bracket there must be a closing bracket
        #and that opening must always precede closing for every pair
        res = []        #O(n) memory complexity
        stack = []
        for ch in s :
            if 'a' <= ch <= 'z':
                res.append(ch)
            elif ch == '(':
                stack.append(ch)
                res.append(ch)
            else:
                if stack:
                    stack.pop()
                    res.append(ch)                 
        if stack:
            i = len(res) - 1
            while stack:
                if res[i] == '(':
                    res.pop(i)
                    stack.pop()
                i -= 1
            return ''.join(res)    
        else:
            return ''.join(res)      
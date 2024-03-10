class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        for ch in t:
            if s:
                if ch == s[0]:    
                    s.pop(0)
            else:
                break        
        return False if s else True         

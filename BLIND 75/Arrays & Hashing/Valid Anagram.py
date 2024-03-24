class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s.lower())
        t = list(t.lower())       
        s.sort()
        t.sort()
        if s == t :
            return True
        else:
            return False    

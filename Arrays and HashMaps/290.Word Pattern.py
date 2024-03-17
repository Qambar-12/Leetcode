class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        else:
            d = {}
            for i in range(len(s)):
                if pattern[i] not in d:
                    d[pattern[i]] = s[i]
                else:
                    if d[pattern[i]] != s[i]:
                        return False   
            if len(d.values()) == len(set(d.values())):
                return True        
        

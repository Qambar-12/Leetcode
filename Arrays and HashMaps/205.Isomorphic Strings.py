class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for ch in range(len(s)):
            if s[ch] not in hashmap :
                if t[ch] not in hashmap.values():
                    hashmap[s[ch]] = t[ch]
                else:
                    return False    
            else:
                if hashmap[s[ch]] != t[ch]:
                    return False       
        return True                

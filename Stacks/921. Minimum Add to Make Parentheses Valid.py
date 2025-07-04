class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        hashmap = {'(':0,')':0}
        for p in s:
            if p == '(':
                hashmap[p] += 1
            else:
                if hashmap['('] == 0:
                    res += 1
                else:
                    hashmap['('] -= 1    
        return res+hashmap['(']            
 
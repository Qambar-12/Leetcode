class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res =  0
        g.sort(),s.sort()
        i = 0
        for j in range(len(s)):
            if i < len(g) :
                if s[j] >= g[i]:
                    res += 1
                    i += 1
            else:
                break        
        return res        

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #using sliding window technique
        res = 0
        currCost = 0
        l = 0
        for r in range(len(s)):
            currCost += abs(ord(s[r]) - ord(t[r]))
            while currCost > maxCost:
                currCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, r - l + 1)  
        return res

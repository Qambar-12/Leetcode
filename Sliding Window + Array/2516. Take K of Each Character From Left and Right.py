class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        #using an array or hashmap to first find the total count of characters in the whole string
        count = [0,0,0]
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        #if not enough characters
        if min(count) < k:
            return -1    

        #we would reverse engineer using sliding window approach 
        #i.e find max size (expand as long as) of window while condition for other chars outside window is still valid
        res = float('inf')  #actual result to return 
        l = 0
        lenStr = len(s)
        for r in range(lenStr):
            count[ord(s[r]) - ord('a')] -= 1
            while min(count) < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1
            res = min(res, lenStr-(r-l+1))    
        return res
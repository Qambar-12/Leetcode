class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #using sliding window technique implemented via two pointers
        #maintaing a hashmap to count freq of each charcter in the window
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf,count[s[r]])
            #or simply max(count.values())
            #while the size of window is not valid i.e we subtract the freq of most repeated character from size of window to get the number of characters we need to replace
            while (r-l+1) - maxf > k:
                #before incrementing the left pointer updating the hashmap
                count[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res        
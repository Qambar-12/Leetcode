class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #for 3-length palindromes (of lower case eng letters) there are possibly 26*26 total ways
        #because we can fix middle character having choices 26 and for each middle character we can continue changing left and right char

        res = set()       #returning its length at the end
        left = set()
        right = collections.Counter(s)          #hashmap
        #time complexity is O(26.n)
        for i in range(len(s)):
            #before checking for right portion we need to remove this middle char val from hashmap
            right[s[i]] -= 1
            if not right[s[i]] :
                right.pop(s[i])
            for j in range(26):
                c = chr(ord('a')+j)
                #i.e we can create a palindromic subsequence
                if c in left and c in right:
                    res.add((c+s[i]+c))
            #before our loop moves to next char val adding it to left hashset 
            left.add(s[i])
        return len(res)            

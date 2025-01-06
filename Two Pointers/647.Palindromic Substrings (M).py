class Solution:
    def countSubstrings(self, s: str) -> int:
        #Two pointer Solution
        # tot = 0
        # for i in range(len(s)):
        #     j = len(s)-1
        #     while i <= j:
        #         st = s[i:j+1]
        #         if st == st[::-1]:
        #             tot += 1
        #         j-=1
        # return tot            

        #Method 2: Finding number of even and odd palindromic substrings and add them together
        #for odd : Imagine the ch as middle of palindrome and expand outwards both to left and right
        #          (as long as they are equal we get odd palindromes of length e.g 1 3 5 7 .... and so on)
        #for even : we start with length of 2 where r = l+1
        # tot = 0
        # for i in range(len(s)):
        #     #odd length palindrome
        #     l = r = i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         tot += 1
        #         l -= 1
        #         r += 1
        #     #even length palindrome
        #     l , r = i , i+1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         tot += 1
        #         l -= 1
        #         r += 1
        # return tot             
        tot = 0
        for i in range(len(s)) :
            tot += self.countPalindromes(s,i,i)
            tot += self.countPalindromes(s,i,i+1)
        return tot    
    def countPalindromes(self,s,l,r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res       

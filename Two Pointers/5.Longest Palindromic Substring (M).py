class Solution:
    def longestPalindrome(self, s: str) -> str:
        #base case
        if s == s[::-1]:
            return s
        res = ''
        #to check for palindrome we could either initialize our pointers to extreme positions and contiue decreasing size of window as long as s[l] == s[r]
        #or more efficient way for this problem is to imagine each character visting as centre of string
        #and continue expanding outwards right and left as long as palindrome and pointers in bound else update the result
        #time complexity O(n^2)
        for ch in range(len(s)):
            l , r = ch , ch
            #while pointers are in bound and equal   ----> checking if odd length palindromic substring
            while (l >= 0 and r < len(s)) and s[l] == s[r]:
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
            #Edge case : even length palindromic substring 
            l , r = ch , ch + 1
            while (l >= 0 and r < len(s)) and s[l] == s[r]:   
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1  
        return res            

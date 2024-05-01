class Solution:
    def shortestPalindrome(self, s: str) -> str:
        #intuitively we can get a palindrome if we reverse the original string and append original string to it or vice versa
        #however our approach must be to find shortest palindrome at first before returning above answer
        if s == s[::-1] : return s
        index = 1
        for i in range(1,len(s)):
           #finding the longest palindrome in the current string and reversing the remaining part and adding it to infront of string
           if s[:i]  == s[:i][::-1]:
               index = i
               
        return s[index:][::-1] + s
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #Sliding window approach
        i,count,res = 0,0,0
        #Hashset
        vowels = {'a','e','i','o','u'}
        for j in range(len(s)):
            count += 1 if s[j] in vowels else 0
            #when size of window gets greater than k incrementing the left pointer i 
            #and decrementing count by 1 if s[i] was a vowel
            #i.e because count is a running total
            if (j-i+1) > k:
                count -= 1 if s[i] in vowels else 0
                i += 1
            res = max(res,count)
        return res    

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
       #Sliding Window approach
       #if null string
       if len(s) == 0 :
           return 0
       else:
           dictChar = {}
           startPointer = 0
           length = 0
           for i in range(len(s)):
               if (s[i] in dictChar) and (startPointer <= dictChar[s[i]]) :
                   #Start pointer updated if the encountered character is already present in dictionary
                   #That means repeated character
                   startPointer = dictChar[s[i]] + 1
               else :
                   # +1 because using range function
                   length = max(length,(i-startPointer+1))
               #Updating the dictionary containing characters (has a key and value)
               dictChar[s[i]] = i
       return length        



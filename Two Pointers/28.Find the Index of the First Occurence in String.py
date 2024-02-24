class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #Two pointer technique
        i,j = 0,len(needle)
        while j <= len(haystack):
            #Slicing
            if haystack[i:j] == needle:
                return i
            else:
                i += 1
                j = i + len(needle)
        return -1            

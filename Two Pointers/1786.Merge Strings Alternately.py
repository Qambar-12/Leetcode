class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged = ''
        while i < min(len(word1),len(word2)):
            merged += (word1[i] + word2[i])
            i += 1
        if len(word1) == len(word2):
            return merged
        elif len(word1) > len(word2):
            merged += word1[i:]
        else:
            merged += word2[i:]
        return merged                

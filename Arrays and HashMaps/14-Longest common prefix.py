class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest= ''
        for word in strs:
            if len(word) > len(longest):
                longest = word
        for word in range(len(strs)):
            while True:
                if len(longest) != 0:
                    if not(strs[word].startswith(longest)):
                        longest = longest[:len(longest)-1]
                    else:
                        break
                else:
                    return ''
        return longest                                                
        


                    


              
 



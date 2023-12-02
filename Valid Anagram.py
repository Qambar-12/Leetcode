class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Making list to let use sort method
        #lower() method used for strings to create a lower case string 
        #upper() method can also be used instead
        #Nested calls
        s = list(s.lower())
        t = list(t.lower())       
        s.sort()
        t.sort()
        if s == t :
            return True
        else:
            return False    

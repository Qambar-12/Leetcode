class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        
        for i in range(len(s)):
            #to avoid index out of range error and observation used is for subtraction cases that following element val is greater 
            if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
                num -= d[s[i]]
            else:
                num += d[s[i]]
        
        return num

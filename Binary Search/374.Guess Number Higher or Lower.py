# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #List = list(range(1,n+1)) (Menory limit exceeded if list used)
        i,j = 0,n
        while i <= j:
            val = (i+j)//2
            if  guess(val) == -1:
                j = val - 1
            elif guess(val) == 1:
                i = val + 1
            else:
                return val       

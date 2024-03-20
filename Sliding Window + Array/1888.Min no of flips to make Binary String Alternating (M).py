class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        #to simulate the condition when we have performed type-1 operation on every possible element in original s given
        #And then finally use a sliding window technique via two-pointer
        s = s + s
        #the only possible forms of alternating strings
        alt1 , alt2 = '',''
        for i in range(len(s)):
            alt1 += '0' if i%2 else '1'
            alt2 += '1' if i%2 else '0'
        flips1,flips2 = 0,0
        l = 0
        #res var will be initialized with max possible so that we can store and return minimum number of flips of operation type-2
        res = len(s)
        for r in range(len(s)):
            if s[r] != alt1[r]:
                flips1 += 1
            if s[r] != alt2[r]:
                flips2 += 1
            #checking the size of window r by r-l+1
            if (r-l+1) > n:
                #before performing type-1 operation i.e incrementing our left pointer checking whether our element on left pointer in alt1 and alt2 respectively match with s[l]
                #if match not found and since we are excluding it from our window we need to decrements our flips variable respectively else simply pass on
                if s[l] != alt1[l]:
                    flips1 -= 1
                if s[l] != alt2[l]:
                    flips2 -= 1
                
                l += 1  

            #if our window size is equal to that of original length of string then we could compute min number of flips
            if (r-l+1) == n:
                res = min(res,flips1,flips2)
        return res 
          
       
       

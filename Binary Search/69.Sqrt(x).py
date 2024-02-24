class Solution:
    def mySqrt(self, x: int) -> int:
        i,j = 0,x
        res = 0
        while i <= j:
            #Or mid = i + ((j-i)//2) prevents overflow
            mid = (i+j)//2
            if mid**2 > x:
                j = mid-1
            elif mid**2 < x:
                i = mid + 1
                res = mid
            else:
                return mid
        #if loop terminates we would have greatest mid squared value that is less than x which is equal to rounding down sqrt
        return res                
            

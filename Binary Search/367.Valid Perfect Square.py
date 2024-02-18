class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i,j = 0,num
        while i<=j:
            mid = (i+j)//2
            if mid**2 > num:
                j = mid - 1
            elif mid**2 < num:    
                i = mid + 1
            else:
                return True
        return False            

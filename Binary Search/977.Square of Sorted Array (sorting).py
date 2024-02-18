class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_sorted = []
        i,j = 0,len(nums)-1
        while i <= j :
            if abs(nums[i]) > abs(nums[j]):
                sq_sorted.insert(0,nums[i]**2)
                i += 1
            elif abs(nums[i]) < abs(nums[j]):
                sq_sorted.insert(0,nums[j]**2)
                j -= 1
            elif (abs(nums[i]) == abs(nums[j])) and (i != j):
                sq_sorted.insert(0,nums[i]**2)
                sq_sorted.insert(0,nums[j]**2)
                i += 1
                j -= 1
            else:
                sq_sorted.insert(0,nums[i]**2)
                i += 1
                j -= 1    
        return sq_sorted            

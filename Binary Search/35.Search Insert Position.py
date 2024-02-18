class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while i <= j:
            index = int((i+j)/2)
            if nums[index] == target:
                return index
            elif nums[index] > target:
                j = index-1
            else:
                i =  index+1
        return i

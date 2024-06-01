class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                for j in range(i,len(nums)-1):
                    if nums[j] > nums[j+1]:
                        return False
                break
            elif nums[i] > nums[i+1]:
                for j in range(i,len(nums)-1):
                    if nums[j] < nums[j+1]:
                        return False
                break
        return True

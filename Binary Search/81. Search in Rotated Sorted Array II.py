class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #there are possibly two sorted portions in the array and runtime of O(logn) usually refers to binary search
        #the portions are namely left and right and we check for these portions by:
        #nums[l] <= mums[mid] then our pointer is in left sorted portion and right otherwise
        #if sorted array is rotated n times it preserves the order of elements
        if nums[0] <= nums[len(nums)-1]:
            return True if target in nums else False
        #Binary search algorithm
        l , r = 0 , len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return True
            #if in left sorted portion
            if nums[l] <= nums[mid]:
                #need to search to the right 
                if target > nums[mid] or target < nums[l] :
                    l = mid + 1
                else:
                    r = mid - 1    
            #if in right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1    
        return False  
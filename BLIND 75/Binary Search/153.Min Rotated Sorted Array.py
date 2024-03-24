class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Binary search time complexity O(logn)
        res = nums[0]
        #Initializing the two pointers
        l , r = 0 , len(nums)-1
        #while the pointers have not crossed eachother
        while l <= r:
            #checking if the whole window in between left and right pointer is sorted then simply min is nums[l]
            if nums[l] <= nums[r]:
                res = min(res,nums[l])
                return res

            #Finding the mid-pointer
            mid = (l+r)//2
            #if l to mid portion is sorted we need to search the right portion and vice versa
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            res = min(res,nums[mid])
        return res                

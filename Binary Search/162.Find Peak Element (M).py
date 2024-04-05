class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """Binary Search Intuation : Either an element is a peak or one of it's neighbour is 
        is guaranteed to be greater than it so we search that side eliminating half of search
        space i.e so algorithm runs in O(logn) time b/c either it would have monotonic increasing trend
        or it would have a dip somewhere in both cases it is guaranteed that this side would have a 
        peak value i.e greater than it's neighbour """
        #Binary Search O(logn)
        #Relative Maxima concept
        l , r = 0, len(nums)-1
        #while pointers have not crossed eachother
        while l <= r:
            #finding midpoint this way prevents overflow
            mid = l + ((r-l)//2)
            #additional checking condition that if our mid is at extreme position so we donot get index out of bound
            if mid < len(nums) - 1 and nums[mid] < nums[mid+1]:
                l = mid + 1
            elif mid > 0 and nums[mid] < nums[mid-1]:
                r = mid - 1
            else:
                break
        return mid                    
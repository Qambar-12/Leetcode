class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #simple binary search algorithm O(logn) time complexity
        #left and right portions to peak array are sorted
        l , r = 0 , len(arr)-1
        #while the pointers have not crossed eachother
        while l <= r:
            mid = l + ((r-l)//2)
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
                

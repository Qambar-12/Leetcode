class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #we can also use Two-pointers approach
        #where i = 0 , j = len(merged)-1
        #ODD --->continue loop until len(merged) == 1
        #EVEN --->continue loop until len(merged) == 2
        #afterwards find the middle
        merged = (nums1+nums2)
        merged.sort()
        #Odd case
        if len(merged) % 2:
            return float(merged[len(merged)//2])
        else:
            #Even case
            midR = len(merged)//2
            midL = midR-1
            return float((merged[midL]+merged[midR])/2)

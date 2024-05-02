class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #alterante way is flatten to 1D list
        """new_m = []
        for m in matrix:
            new_m += m     
        return heapq.nsmallest(k, new_m)[-1]"""
        #using binary search 
        #smallest element ---> Top left
        #largest element ---> Bottom right
        # nxn square matrix where n = len(matrix)
        l , r , n = matrix[0][0] , matrix[-1][-1] , len(matrix)
        #the function basically uses a bisect_right function to check how many elements are less than the mid calculated during binary search
        #condition to use bisect function is sorted order of list
        def count_elements(mid):
            count = 0
            for row in matrix:
                x = bisect_right(row,mid)
                count += x        
            return count
        while l < r:
            mid = (l+r)//2
            #i.e we can find out more elements 
            if count_elements(mid) < k:
                l = mid + 1    
            #we have found more elements than k required
            else:
                r = mid
        return l            

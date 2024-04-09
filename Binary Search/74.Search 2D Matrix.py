class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary search --> O(logm) where m is the number of rows
        #however since binary search also runs on each of columns n in a particular row
        #overall time complexity is O(log(m*n))
        l , r = 0 , len(matrix)-1
        while l <= r:
            #finding mid this way instead of (l+r)//2 prevents overflow in case
            midRow = l + ((r-l)//2)
            i , j = 0 , len(matrix[midRow])-1
            if matrix[midRow][i] <= target <= matrix[midRow][j]:
                if matrix[midRow][i] == target or matrix[midRow][j] == target:
                    return True
                else:
                    while i <= j:
                        midCol = i + ((j-i)//2)
                        if matrix[midRow][midCol] < target:
                            i = midCol + 1
                        elif matrix[midRow][midCol] > target:
                            j = midCol - 1
                        else:
                            return True 
                    return False        
            elif target < matrix[midRow][i]:
                r = midRow - 1
            else:
                l = midRow + 1    
        return False

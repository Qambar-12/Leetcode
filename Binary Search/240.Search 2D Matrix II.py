class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Slightly different from conventional binary search
        #we need to find the criteria for eliminating the search space basically
        #each row is sorted in ascending order
        #each column is also sorted in ascending order
        #however rows that follow eachother are not sorted 
        #starting point for search  ----> either row 0 and col[-1] because from left to right and from top to bottom whole sequence of integers is sorted
                                    #    or row[-1] and col 0 because from top to bottom and then from left to right whole sequence of integers is sorted aswell
        r , c = 0 , len(matrix[0])-1
        #the loop runs until we reach the last diagonal element on the other end
        while r <= len(matrix)-1 and c >= 0 :
            if matrix[r][c] == target :
                return True
            #if cell value is less than target we can discard the left part of the row hence incrementing row value
            elif matrix[r][c] < target :
                r += 1
            #if cell value is greater than target we can discard bottom part of column hence decrementing the columnn value
            else:
                c -= 1        
        return False
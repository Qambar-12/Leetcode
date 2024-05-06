"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        #Quad tree node has attributes : val , isLeaf , topLeft , topRight , bottomLeft , bottomRight
        #if isLeaf is True it is implied that all children will be None
        #we need to continue dividing grid into 4 quadrants recursively until each of cells in quad have same value and that is our base case i.e leaf node
        #DFS recursive algorithm
        #n = dimension of sub-square grid and row and col are topleft coordinates of that grid
        def dfs(n,row,col):
            #base case check that if all are same in a particular quadrant then its a leaf node
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row + i][col + j]:
                        allSame = False
                        break
            #i.e a leaf node and all childs are implied to be Null
            if allSame:
                return Node(grid[row][col],True)
            #we recursively need to divide quadrant more
            else:
                n //= 2
                topLeft = dfs(n,row,col)
                topRight = dfs(n , row , col+n)
                bottomLeft = dfs(n,row+n,col)
                bottomRight = dfs(n , row + n , col+n)
                return Node(0,False,topLeft,topRight,bottomLeft,bottomRight)
        return dfs(len(grid),0,0)        
                

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #to detect duplicates in any of row or col or 3x3 square matrix we use a hashmap
        #where (key : val) pair is a row or col or matrix and val is a hashset
        row = defaultdict(set)
        col = defaultdict(set)
        square_grid = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in row[r]) or (board[r][c] in col[c]) or (board[r][c] in square_grid[(r//3 , c//3)]):
                    return False
                row[r].add(board[r][c])   
                col[c].add(board[r][c])
                square_grid[(r//3 , c//3)].add(board[r][c])
        return True        

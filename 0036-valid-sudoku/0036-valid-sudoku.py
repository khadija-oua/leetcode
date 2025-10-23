from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        n = defaultdict(set)
        m = defaultdict(set)
        p = defaultdict(set)
        for i in range (9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in n[i] or board[i][j] in m[j] or  board[i][j] in  p[(i//3,j//3)]:
                     return False 
                n[i].add(board[i][j])
                m[j].add(board[i][j])
                p[(i//3,j//3)].add(board[i][j])
    
        return True

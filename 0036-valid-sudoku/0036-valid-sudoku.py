class Solution(object):
    def isValidSudoku(self, board):
         #rows
        for i in range (9):
            n = set()
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in n : return False 
                    else : n.add(board[i][j])
        #columns
        for i in range (9):
            n =  set()
            for j in range(9):
                if board[j][i]!=".":
                    if board[j][i] in n : return False 
                    else : n.add(board[j][i])
        #squares 
        data = {}
        for i in range (9):
            for j in range(9):
                key = (i//3,j//3)
                if board[i][j]!=".":
                    if  board[i][j] in  data.get(key, set()):
                        return False 
                    else : 
                        data.setdefault(key, set()).add(board[i][j])
        return True

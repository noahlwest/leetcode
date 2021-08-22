class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check that all the squares are valid
        for i in range(0, 3):
            for j in range(0, 3):
                cur = board[i*3][j*3 : (j+1)*3]
                cur += board[i*3 +1][j*3 : (j+1)*3]
                cur += board[i*3 +2][j*3 : (j+1)*3]
                cache = {}
                for element in cur:
                    if element.isnumeric() and element in cache:
                        return False
                    else:
                        cache.update({element : "_"})
        
        #check that all the rows are valid
        for row in board:
            cache = {}
            for element in row:
                if element.isnumeric() and element in cache:
                    return False
                else:
                    cache.update({element : "_"})
        
        #check that all the columns are valid
        for i in range(0, 9):
            cache = {}
            for j in range(0, 9):
                if board[j][i].isnumeric() and board[j][i] in cache:
                    return False
                else:
                    cache.update({board[j][i] : "_"})
        
        return True

#runtime: O(1)
#memory: O(1)
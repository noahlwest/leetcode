class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        self.rows = len(board)
        self.columns = len(board[0])
        self.board = board
    
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                if board[i][j] == word[0]:
                    res = self.search(board, i, j, word)
                    if res == True:
                        return True
                    
        return False
    
    def search(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i >= self.rows or j >= self.columns or i < 0 or j < 0:
            return False
        if board[i][j] != word[0]:
            return False
        board_char = board[i][j]
        board[i][j] = "Visited"
        result = self.search(board, i+1, j, word[1:]) or self.search(board, i-1, j, word[1:]) or self.search(board, i, j+1, word[1:]) or self.search(board, i, j-1, word[1:])
        board[i][j] = board_char
        return result
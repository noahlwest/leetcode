class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        #go around all the edges, and dfs all the Os that are connected, mark them as non-capturable
        self.board = board
        self.safe_spaces = {}
        
        self.rows = len(board)
        self.columns = len(board[0])
        
        #mark the first and last columns
        for i in range(0, self.rows):
            if board[i][0] == 'O' and (i, 0) not in self.safe_spaces:
                self.mark_connected_as_safe(i, 0)
            if board[i][self.columns-1] == 'O' and (i, self.columns-1) not in self.safe_spaces:
                self.mark_connected_as_safe(i, self.columns-1)
                
        #mark the first and last rows
        for i in range(0, self.columns):
            if board[0][i] == 'O' and (0, i) not in self.safe_spaces:
                self.mark_connected_as_safe(0, i)
            if board[self.rows-1][i] == 'O' and (self.rows-1, i) not in self.safe_spaces:
                self.mark_connected_as_safe(self.rows-1, i)
                
        #now that all pieces should be marked, loop through and capture them
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                if (i, j) not in self.safe_spaces:
                    board[i][j] = 'X'
            
    def mark_connected_as_safe(self, row, column):
        if (row, column) in self.safe_spaces:
            return
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            return
        if self.board[row][column] == 'O':
            self.safe_spaces[(row, column)] = "_"
            self.mark_connected_as_safe(row-1, column)
            self.mark_connected_as_safe(row+1, column)
            self.mark_connected_as_safe(row, column-1)
            self.mark_connected_as_safe(row, column+1)
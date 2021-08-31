class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        columns = n
        #there is only one possible path for directly right and directly down
        #use those to determine how many paths there are for the other 
        grid = [[1]*columns]*rows
        
        for i in range(1, rows):
            for j in range(1, columns):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                
        return grid[rows-1][columns-1]
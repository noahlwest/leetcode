class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        
        dp = [[0 for i in range(columns)] for i in range(rows)]
        
        for i in range(0, rows):
            for j in range(0, columns):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0 and j > 0:
                    dp[i][j] += grid[0][j] + dp[0][j-1]
                elif i > 0 and j == 0:
                    dp[i][j] += grid[i][0] + dp[i-1][0]
                else:
                    dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])
        
        return dp[rows-1][columns-1]

    #runtime: O(nm)
    #memory: O(nm)
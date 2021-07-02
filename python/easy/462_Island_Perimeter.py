class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #each box starts with 4 edges to add to perimeter
        #for each connected box, remove 1 edge
        
        #if row == 0: do not check for top edge
        #if row == len(grid)-1: do not check for bottom edge
        #if column == 0: do not check for left edge
        #if column == len(row)-1: do not check for right edge
        
        perimeter = 0
        
        for row in range(0, len(grid)):
            for column in range(0, len(grid[row])):
                edges = 4
                if grid[row][column] == 0:
                    continue
                if row != 0:
                    if grid[row-1][column] == 1:
                        edges -= 1
                if row != len(grid)-1:
                    if grid[row+1][column] == 1:
                        edges -= 1
                if column != 0:
                    if grid[row][column-1] == 1:
                        edges -= 1
                if column != len(grid[row])-1:
                    if grid[row][column+1] == 1:
                        edges -= 1
                perimeter += edges
                
        return perimeter

#runtime: O(n)
#memory: O(1)
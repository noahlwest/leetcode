class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #search down, then right
        
        row = 0
        for i in range(0, len(matrix)):
            if matrix[i][0] <= target:
                row = i
        
        for j in range(0, len(matrix[row])):
            if matrix[row][j] == target:
                return True
            
        return False

    #runtime: O(n + m)
    #memory: O(1)
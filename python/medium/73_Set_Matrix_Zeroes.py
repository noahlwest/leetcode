class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #make groups of rows and columns to set to 0
        rows = {}
        columns = {}
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.update({i : "_"})
                    if j not in columns:
                        columns.update({j : "_"})
                        
        for key, value in rows.items():
            for i in range(0, len(matrix[key])):
                matrix[key][i] = 0
                
        for key, value in columns.items():
            for i in range(0, len(matrix)):
                matrix[i][key] = 0

    #runtime: O(n*m)
    #memory: O(n+m)
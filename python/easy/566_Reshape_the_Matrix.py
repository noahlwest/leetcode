class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ret = [[]]
        row_c = 0
        col_c = 0
        
        total_length = sum(len(row) for row in mat)
        if total_length != (r * c):
            return mat
        
        for row in mat:
            for column in row:
                if col_c == c:
                    col_c = 0
                    row_c += 1
                    ret.append([])
                print(col_c, row_c)
                ret[row_c].append(column)
                col_c += 1
                
        return ret

#runtime: O(2n) -> O(n)
#memory: O(n)
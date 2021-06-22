class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        #for each row
            #for each index in the row
            
        ret = []
        for i in range(0, numRows):
            ret.append([])
            
        for i in range(0, numRows):
            for j in range(0, i+1):
                if j == 0 or j == i:
                    ret[i].append(1)
                else:
                    ret[i].append(ret[i-1][j-1] + ret[i-1][j])
                    
        return ret
                    
#runtime: O(n) + O(n * n) = O(n^2)
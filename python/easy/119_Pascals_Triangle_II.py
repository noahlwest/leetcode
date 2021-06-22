class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        #create the full pascals triangle
        ret = []
        for i in range(0, rowIndex+1):
            ret.append([])
            
        for i in range(0, rowIndex+1):
            for j in range(0, i+1):
                if j == 0 or j == i:
                    ret[i].append(1)
                else:
                    ret[i].append(ret[i-1][j-1] + ret[i-1][j])
            if i == rowIndex:
                return ret[i]

#runtime: O(n^2)
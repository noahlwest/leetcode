class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #basically convert to base 26
        
        ret = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            ret = chr((columnNumber % 26) + 65) + ret
            columnNumber = columnNumber // 26
            
            
        return ret
            
#runtime: O(log n) input is // 26 each time
#memory: O(1) 
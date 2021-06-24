class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #convert base 26 to base 10
        
        ret = 0
        
        for i in range(0, len(columnTitle)):
            ret += (ord(columnTitle[-(i+1)]) - 64) * 26**i
            
        return ret

#runtime: O(n)
#memory: O(1)
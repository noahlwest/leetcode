class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        while x > 0 or y > 0:
            if x > 0 and y > 0:
                if x % 2 != y % 2:
                    ret += 1
                x = x // 2
                y = y // 2
            elif x > 0:
                if x % 2 == 1:
                    ret += 1
                x = x // 2
            else:
                if y % 2 == 1:
                    ret += 1
                y = y // 2
                    
        return ret
                
#runtime: O(log n)
#memory: O(1)
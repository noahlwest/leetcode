class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 1
        while n > 0:
            n -= rows
            rows += 1
        rows -= 1
        if n == 0:
            return rows
        return rows-1

#runtime: O(n)? 
#memory: O(1)
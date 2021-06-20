class Solution:
    def climbStairs(self, n: int) -> int:
        i, j = 1, 1
        for k in range(n):
            i,j = j, i + j
        return i

#runtime: O(n)
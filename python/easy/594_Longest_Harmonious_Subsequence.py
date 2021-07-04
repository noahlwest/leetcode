class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        if ops == []:
            return m * n
        else:
            return min(i[0] for i in ops) * min(i[1] for i in ops)
#runtime: O(2n) -> O(n)
#memory: O(1)
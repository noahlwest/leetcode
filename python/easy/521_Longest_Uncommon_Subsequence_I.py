class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a != b:
            return max(len(a), len(b))
        else:
            return -1

#runtime: O(1) (strings limited to 100 in length)
#memory: O(1)
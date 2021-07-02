class Solution:
    def checkRecord(self, s: str) -> bool:
        L = 0
        A = 0
        for char in s:
            if char == "P":
                L = 0
            if char == "A":
                A += 1
                L = 0
                if A >= 2:
                    return False
            if char == "L":
                L += 1
                if L >= 3:
                    return False
            
        return True

#runtime: O(n)
#memory: O(1)
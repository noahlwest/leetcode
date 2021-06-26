class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(0, 46341):
            if num == i*i:
                return True
            
        return False

#runtime: O(1) (still slow, though)
#memory: O(1)
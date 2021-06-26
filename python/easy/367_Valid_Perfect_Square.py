class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = 46341
        while left < right:
            middle = (left + right) // 2
            if num == middle*middle:
                return True
            elif num > middle*middle:
                left = middle+1
            else: #num < middle*middle:
                right = middle
            
        return False

#runtime: O(1) [has a constant cap on execution time, but it's faster than linear O(1)]
#memory: O(1)
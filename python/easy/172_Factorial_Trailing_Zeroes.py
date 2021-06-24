class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = factorial(n)
        counter = 0
        while x % 10 == 0:
            counter += 1
            x = x //10
            
        return counter

#runtime: O(n)
#memory: O(1)
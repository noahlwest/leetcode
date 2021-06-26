class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            copy = num
            sum = 0
            while copy > 0:
                sum += copy % 10
                copy = copy // 10
            num = sum
        return num
        
#runtime: Not sure how to calculate this
#memory: O(1)
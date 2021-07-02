class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        ret = 0
        counter = 0
        while num > 0:
            ret += (2**counter) * (1 - (num % 2))
            num = num // 2
            counter += 1
        return ret
            
#runtime: O(log n)
#memory: O(1)
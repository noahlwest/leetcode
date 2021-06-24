class Solution:
    def hammingWeight(self, n: int) -> int:
        #divide by 2
        #get the last bit (modulo 2 it)
        count = 0
        while n > 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
            
        return count

#runtime: O(1) (always same size input)
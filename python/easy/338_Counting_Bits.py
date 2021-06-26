class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        for i in range(0, n+1):
            sum = 0
            while i > 0:
                sum += i % 2
                i = i // 2
                    
            ret.append(sum)
            
        return ret
            
#runtime: O(n)
#memory: O(n)
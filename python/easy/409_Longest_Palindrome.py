class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        #max int = 4294967296
        #normalize to unsigned
        if num < 0:
            num += 4294967296
        
        digits = "0123456789abcdef"
        
        ret = ""
        
        while num > 0:
            rem = num % 16
            num = (num - rem)//16
            ret = digits[rem] + ret

        return ret
            
#runtime: O(2n) -> O(n)
#memory: O(n)
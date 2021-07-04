class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        is_negative = False
        if num < 0:
            num *= -1
            is_negative = True
            
        ret = ""
        while num > 0:
            ret = str(num % 7) + ret
            num = num // 7
        
        if is_negative == True:
            ret = "-" + ret
        return ret

#runtime: O(log n)
#memory: O(1)
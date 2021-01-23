class Solution:
    def reverse(self, x: int) -> int:
        
        if(x < 10 and x > -10):
            return x
        
        is_negative = False
        if(x < 0):
            is_negative = True
            x = x * -1
        
        new_num = 0
        while(x):
            new_num += (x % 10)
            x = (x // 10)
            if(x):
                if(new_num > 214748364.7):
                    return 0
                new_num *= 10
        
        if is_negative:
            return new_num * -1
        else:
            return new_num

#runtime: O(log(x))
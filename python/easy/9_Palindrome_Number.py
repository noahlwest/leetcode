class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        
        if(x >= 0 and x <= 9):
            return True
        
        if(x % 10 == 0):
            return False
        
        x_reverse = 0
        while(x > x_reverse):
            x_reverse *= 10
            x_reverse += x % 10
            x = x // 10
            
        if(x == x_reverse) or (x == x_reverse//10):
            return True
            
        return False

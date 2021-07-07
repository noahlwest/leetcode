class Solution:
    def myAtoi(self, s: str) -> int:
        
        strlen = len(s)
        if strlen == 0:
            return 0
        
        #use a pointer to first get past the leading whitespace
        ptr = 0
        while ptr < strlen and s[ptr] == " ":
            ptr += 1
    
        #check if there are any numbers left
        if ptr == strlen:
            return 0
        
        #check if the first non-whitespace char is a + or -
        is_negative = False
        if s[ptr] == "-":
            is_negative = True
            ptr += 1
        elif s[ptr] == "+":
            ptr += 1
        
        #read in the numbers, multiply by 10 as necessary
        ret = 0
        while ptr < strlen and s[ptr].isnumeric():
            ret *= 10
            ret += int(s[ptr])
            ptr += 1
        
        if is_negative == True:
            ret *= -1
            
        #verify it will fit in int_32
        if ret < -2147483648:
            return -2147483648
        if ret > 2147483647:
            return 2147483647
        
        return ret

#runtime: O(n)
#memory: O(1)
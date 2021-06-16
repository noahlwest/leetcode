class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #start at the end
        
        #0 = 48, 1 = 49
        
        #while there are still numbers to add:
            #sum = a[i] + b[i] + carryout
            #4 cases: sum == 0, 1, 2, 3
            
        index_a = len(a) - 1
        index_b = len(b) - 1
        
        ret_string = ""
        
        carry_out = 0
        
        while index_a >= 0 or index_b >= 0:
            if index_a >= 0 and index_b >= 0:
                sum = int(a[index_a]) + int(b[index_b]) + carry_out
            elif index_a >= 0:
                sum = int(a[index_a]) + carry_out
            else:
                sum = int(b[index_b]) + carry_out
        
            #4 cases: (0, 1, 2, 3)
            if sum == 0:
                ret_string = "0" + ret_string
                carry_out = 0
            elif sum == 1:
                ret_string = "1" + ret_string
                carry_out = 0
            elif sum == 2:
                ret_string = "0" + ret_string
                carry_out = 1
            else:
                ret_string = "1" + ret_string
                carry_out = 1
            
            index_a -= 1
            index_b -= 1

        
        if carry_out == 1:
            ret_string = "1" + ret_string
            
        return ret_string

#runtime: O(n)
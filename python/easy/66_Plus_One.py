class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        counter_from_end = 0
        index = len(digits)-1
        
        digits[index] += 1
        result = digits[index]
        
        while result > 9:
            digits[index] = 0
            index -= 1
            #carryout goes beyond the start of our array
            if index == -1:
                return [1] + digits
            digits[index] += 1
            result = digits[index]
            
        
        return digits

#runtime: O(n)
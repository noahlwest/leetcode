class Solution:
    def romanToInt(self, s: str) -> int:
        
        val = 0
        previous_char = 0
        for i, char in enumerate(s):
            if(char == 'I'):
                val += 1
                previous_char = 'I'
            if(char == 'V'):
                if(previous_char == 'I'): val -= 2
                val += 5
                previous_char = 'V'
            if(char == 'X'):
                if(previous_char == 'I'): val -= 2
                val += 10
                previous_char = 'X'
            if(char == 'L'):
                if(previous_char == 'X'): val -= 20
                val += 50
                previous_char = 'L'
            if(char == 'C'):
                if(previous_char == 'X'): val -= 20
                val += 100
                previous_char = 'C'
            if(char == 'D'):
                if(previous_char == 'C'): val -= 200
                val += 500
                previous_char = 'D'
            if(char == 'M'):
                if(previous_char == 'C'): val -= 200
                val += 1000
                previous_char = 'M'
                
        return val

#time: O(s)
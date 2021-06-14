class Solution:
    def isValid(self, s: str) -> bool:
        #dictionary of closing brackets and their matching opening brackets
        closing_brackets = {")": "(", "]": "[", "}": "{"}
        
        #for each char in string
            #if char is opening bracket:
                #add to stack
            #else:
                #if stack is not empty:
                    #pop from stack and check if characters match
                #if stack is empty:
                    #return false
            
        #create stack for matching brackets
        stack = []
            
        
        for char in s:
            if char not in closing_brackets:
                stack.append(char)
            else:
                if not bool(stack):
                    return False #closing bracket with no matching opening bracket
                else:
                    matching_char = stack.pop()
                    if not matching_char == closing_brackets.get(char):
                        #closing bracket does not match opening bracket
                        return False
        
        if bool(stack):
            return False
                    
        return True
    
#runtime: O(n)
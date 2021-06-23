class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        #first: isolate s to only alphanumeric
        new_str = ""
        if not s.isalnum():
            for char in s:
                if str(char).isalnum():
                    new_str += char
        else:
            new_str = s
    
        new_str = new_str.lower()
        
        start = 0
        end = len(new_str)-1
        
        while start < end:
            if new_str[start] == new_str[end]:
                start += 1
                end -= 1
            else:
                return False
            
        return True

#runtime: O(n)
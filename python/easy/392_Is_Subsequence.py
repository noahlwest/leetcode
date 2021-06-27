class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        s_index = 0
        t_index = 0
        for i in range(0, len(s)):
            while t_index < len(t) and s[s_index] != t[t_index]:
                t_index += 1
            
            if t_index == len(t):
                break
            
            s_index += 1
            t_index += 1
            
        if s_index != len(s):
            return False
        return True
        
#runtime: O(n)
#memory: O(1)
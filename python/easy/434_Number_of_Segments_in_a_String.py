class Solution:
    def countSegments(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        i = 0
        ret = 0
        while i < len(s):
            if s[i] == " " and s[i-1] != " ":
                if i != 0:
                    ret += 1
            i += 1
        if s[len(s)-1] != " ":
            ret += 1
        return ret

#runtime: O(n)
#memory: O(1)
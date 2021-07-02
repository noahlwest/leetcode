class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ret = ""
        length = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] != '-':
                if length % k == 0 and length != 0:
                    ret = s[i] + "-" + ret
                    length += 1
                else:
                    ret = s[i] + ret
                    length += 1    
        return ret.upper()

#runtime: O(n)
#memory: O(1) (O(n) for string size?)
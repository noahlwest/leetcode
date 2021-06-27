class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        
        
        for i in range(0,len(s)):
            if seen[s[i]] == 1:
                return i
            
        return -1
#runtime: O(n) -> O(2n)
#memory: O(n)
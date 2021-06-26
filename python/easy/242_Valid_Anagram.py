class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        stash = {}
        for char in s:
            if char in stash:
                stash.update({char : stash[char]+1})
            else:
                stash.update({char : 1})
                
        for char in t:
            if char in stash:
                if stash[char] == 0:
                    return False
                else:
                    stash.update({char : stash[char]-1})
            else:
                return False
            
        return True

#runtime: O(2n) -> O(n)
#memory: O(n)
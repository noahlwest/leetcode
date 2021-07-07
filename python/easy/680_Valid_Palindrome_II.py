class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        used_skip = False
        resettable = True
        left = 0
        right = len(s)-1
        cached_left = None
        cached_right = None
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1 
            elif s[left] != s[right] and used_skip == False:
                if s[right-1] == s[left]:
                    cached_left = left
                    cached_right = right
                    used_skip = True
                    right -= 1
                elif s[left+1] == s[right]:
                    cached_left = left
                    cached_right = right
                    used_skip = True
                    left += 1
                else:
                    return False
            elif resettable == True:
                left = cached_left
                right = cached_right
                resettable = False
                if s[right-1] == s[left]:
                    left += 1
                elif s[left+1] == s[right]:
                    right -= 2
                else:
                    return False
                    
            else:
                return False
            
        return True

#runtime: O(n)
#memory: O(1)
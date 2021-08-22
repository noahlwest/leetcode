class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        ret = s[0]
        for i in range(0, length):
            is_palindrome = False
            left, right = 0, 0
            curr = ""
            #if "center palindrome"
            if(i-1 >= 0 and i+1 < length) and (s[i-1] == s[i+1]):
                is_palindrome = True
                curr = s[i]
                left = i-1
                right = i+1
                
                while(left >= 0 and right < length) and (is_palindrome == True):
                    if s[left] == s[right]:
                        curr = s[left] + curr + s[right]
                        if len(curr) > len(ret):
                            ret = curr
                        left -= 1
                        right += 1
                    else:
                        is_palindrome = False
                        
            #if "adjacent palindrome"
            if(i+1 < length) and (s[i] == s[i+1]):
                is_palindrome = True
                curr = ""
                left = i
                right = i+1
                
                while(left >= 0 and right < length) and (is_palindrome == True):
                        if s[left] == s[right]:
                            curr = s[left] + curr + s[right]
                            if len(curr) > len(ret):
                                ret = curr
                            left -= 1
                            right += 1
                        else:
                            is_palindrome = False
                        
        return ret

#runtime: O(n^2)?
#memory: O(n)
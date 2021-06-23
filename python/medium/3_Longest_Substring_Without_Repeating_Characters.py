class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                
        longest_substring = 0
        cur_string = ""
        i = 0
        while i < len(s):
            if s[i] in cur_string:
                if longest_substring < len(cur_string):
                    longest_substring = len(cur_string)
                    
                #decide where to cut string
                index = 1
                for j in range(0, len(cur_string)):
                    if cur_string[j] == s[i]:
                        index = j
                if index < len(cur_string):
                    cur_string = cur_string[index+1:]
                else:
                    cur_string = ""
            if not s[i] in cur_string:
                cur_string += s[i]

            i += 1
            
        if longest_substring < len(cur_string):
            return len(cur_string)
            
        return longest_substring
                    
#runtime: O(n)
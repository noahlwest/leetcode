class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #keep a counter for starting position
        #for each index in haystack, try to match the needle
        
        #edge case: no needle
        if needle == "":
            return 0
        #edge case: needle == haystack
        if needle == haystack:
            return 0
        
        for i in range(0, len(haystack) - len(needle) + 1):
            sub_counter = 0
            while sub_counter < len(needle) and needle[sub_counter] == haystack[i + sub_counter]:
                sub_counter += 1
            if sub_counter == len(needle):
                return i
            
        return -1
        
#runtime: O(n)
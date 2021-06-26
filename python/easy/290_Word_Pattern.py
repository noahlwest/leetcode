class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_list = s.split(" ")
        
        cache = {}
        in_pattern = ""
        #current_pattern_char = "a"
        pattern_counter = 0
        for string in str_list:
            if pattern_counter == len(pattern):
                return False
            if string in cache:
                if cache[string] != pattern[pattern_counter]:
                    return False
                in_pattern = in_pattern + cache[string]
            else:
                if pattern[pattern_counter] in cache.values():
                    return False
                cache.update({string : pattern[pattern_counter]})
                in_pattern = in_pattern + pattern[pattern_counter]
            pattern_counter += 1
        
        #print(in_pattern)
        return in_pattern == pattern

#runtime: O(n)
#memory: O(n)
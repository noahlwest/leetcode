class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        #edge case: len(s) == 1
        if len(s) == 1 and s is not " ":
            return 1
        
        current_length = 0
        last_word_length = -1
        last_char_space = False
        space_at_end = False
        
        for i in range(0, len(s)):
            if s[i] != " ":
                last_char_space = False
                current_length += 1
            else:
                if last_char_space:
                    continue
                else:
                    last_word_length = current_length
                    current_length = 0
                    last_char_space = True
        
        #cases: ends in a space or doesn't
        if last_char_space == False:
            return current_length
        else:
            return last_word_length

#runtime: O(n)
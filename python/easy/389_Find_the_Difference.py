class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        extra_char = 0
        
        for i in range(0, len(s)):
            extra_char -= ord(s[i])
            extra_char += ord(t[i])
        return chr(extra_char + ord(t[-1]))

#runtime: O(n) leetcode runtimes aren't that much better than cache method. (36 min cache vs 32 min this method). Likely due to sample sizes
#memory: O(1) memory usage also not that much better. (typically higher! on leetcode) Likely due to sample sizes
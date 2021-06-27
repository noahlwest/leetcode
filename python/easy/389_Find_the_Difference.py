class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cache = {}
        for char in s:
            if char in cache:
                cache[char] += 1
            else:
                cache[char] = 1
        
        for char in t:
            if char in cache:
                if cache[char] == 0:
                    return char
                else:
                    cache[char] -= 1
            else:
                return char

#runtime: O(2n) -> O(n)
#memory: O(n)

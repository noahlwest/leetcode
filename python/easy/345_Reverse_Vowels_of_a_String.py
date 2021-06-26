class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a':'_', 'e':'_', 'i':'_', 'o':'_', 'u':'_', 'A':'_', 'E':'_', 'I':'_', 'O':'_', 'U':'_'}
        string = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            if string[left] in vowels and string[right] in vowels:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
            elif string[left] in vowels:
                right -= 1
            elif string[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        ret = ""
        return ret.join(string)

#runtime: O(n)
#memory: O(n)
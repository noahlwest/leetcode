class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_set = {}
        for char in magazine:
            if char in note_set:
                note_set[char] += 1
            else:
                note_set[char] = 1
            
        print(note_set)
            
        for char in ransomNote:
            if char in note_set:
                if note_set[char] > 0:
                    note_set.update({char : note_set[char]-1})
                else:
                    return False
            else:
                return False
            
        return True

#runtime: O(n + m)
#memory: O(n)
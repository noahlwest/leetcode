class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        #3 acceptable cases:
        #ALL CAPITALS
        if word.isupper():
            return True
        
        #all lowers
        if word.islower():
            return True
        
        #first capital then lowers
        for i in range(0, len(word)):
            if i == 0:
                if not word[i].isupper():
                    return False
            else:
                if not word[i].islower():
                    return False
                
        return True

#runtime: O(n)
#memory: O(1)
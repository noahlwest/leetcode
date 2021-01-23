class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if(not strs):
            return ""
        starter = strs[0]
        ret = ""
        match = True
        for index, char in enumerate(starter):
            for string in strs:
                if(match == False):
                    break
                if(index >= len(string)):
                    match = False
                    break
                if(char != string[index]):
                    match = False
                    break
            if(match == True):
                ret = ret + char
            else:
                break
                
        return ret

#worst case: n identical strings of n length
#runtime: O(n^2)
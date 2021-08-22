class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letter_map = {'2' : ['a', 'b', 'c'], '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], '5' : ['j', 'k', 'l'], '6' : ['m', 'n', 'o'], '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'], '9' : ['w', 'x', 'y', 'z']}        
        combo_list = []
        for i in range(0, len(digits)):
            combo_list.append(letter_map[digits[i]])
        
        uncombined_list = list(itertools.product(*combo_list))
        
        ret = []
        for item in uncombined_list:
            ret.append("".join(item))
            
        return ret        

#runtime: O(n^2)
#memory: O(n)
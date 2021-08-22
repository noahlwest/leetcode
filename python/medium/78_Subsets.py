class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ret = [[]]
        #at each step: adds current number to everything in list (while preserving current list)
        for num in nums:
            length = len(ret)
            for i in range(0, length):
                ret.append(ret[i] + [num])
                
        return ret

#runtime: O(n^2)
#memory: O(n^2?)
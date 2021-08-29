class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        nums.sort()
        #at each step: adds current number to everything in list (while preserving current list)
        for num in nums:
            length = len(ret)
            for i in range(0, length):
                if ret[i] + [num] not in ret:
                    ret.append(ret[i] + [num])
                
        return ret
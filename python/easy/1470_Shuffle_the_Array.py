class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        middle = n
        i = 0
        ret = []
        while middle < len(nums):
            ret.append(nums[i])
            ret.append(nums[middle])
            i += 1
            middle += 1
        return ret
            
#runtime: O(n)
#memory: O(n)
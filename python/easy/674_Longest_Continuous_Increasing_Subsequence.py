class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        curr = 1
        ret = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                ret = max(curr, ret)
                curr = 1
        ret = max(curr, ret)
                
        return ret

#runtime: O(n)
#memory: O(1)
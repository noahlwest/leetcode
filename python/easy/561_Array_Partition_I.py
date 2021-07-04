class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #sort the nums, then take them as pairs from 0
        nums.sort()
        ret = 0
        for i in range(0, len(nums), 2):
            ret += min(nums[i], nums[i+1])
            
        return ret

#runtime: O(n/2) -> O(n)
#memory: O(1)
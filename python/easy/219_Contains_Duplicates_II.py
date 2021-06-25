class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == len(set(nums)):
            return False
        
        if len(nums) <= k + 1:  # k is big enough to cover the whole list
            return True
        
        cache = {}
        
        for i in range(0, len(nums)):
            if nums[i] in cache:
                if abs(i - cache[nums[i]]) <= k:
                    return True
                cache.update({nums[i] : i})
            else:
                cache.update({nums[i] : i})
                
        return False

#runtime: O(2n) = O(n)
#memory: O(n)
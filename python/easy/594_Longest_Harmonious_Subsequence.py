class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        cache = {}
        for num in nums:
            if num in cache:
                cache[num] += 1
            else:
                cache.update({num : 1})
        ret = 0
        for key, value in cache.items():
            ret = max(ret, value + cache.get(key+1, -100000))
        
        return ret

#runtime: O(2n) -> O(n)
#memory: O(n)
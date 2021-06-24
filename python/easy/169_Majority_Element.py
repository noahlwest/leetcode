class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cache = {}
        n = len(nums)
        
        for num in nums:
            if num in cache:
                counter = cache[num] + 1
                if counter > n//2:
                    return num
                else:
                    cache.update({num : counter})
            else:
                if n == 1:
                    return num
                cache.update({num : 1})
                
#runtime: O(n)
#memory: O(n)
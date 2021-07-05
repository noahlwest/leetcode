class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cache = {}
        repeat = -1
        for num in nums:
            if num in cache:
                repeat = num
            else:
                cache.update({num : "_"})
                
        missing = -1
        for i in range(1, len(nums)+1):
            if i not in cache:
                missing = i

        return [repeat, missing]

#runtime: O(2n) -> O(n)
#memory: O(n)
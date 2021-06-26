class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cache = {}
        minimum = 10001
        maximum = -1
        
        for num in nums:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
            cache.update({num : "_"})
            
        if minimum > 0:
            return 0
            
        for i in range(minimum, maximum):
            if i not in nums:
                return i
        
        return maximum+1        
#runtime: O(2n) -> O(n)
#memory: O(n)
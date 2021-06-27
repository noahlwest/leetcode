class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        cache = set()
        for num in nums:            
            cache.add(num)
            
        ret = []
        
        for i in range(1, len(nums)+1):
            if i not in cache:
                ret.append(i)
                
        return ret

#runtime: O(2n) -> O(n)
#memory: O(n)
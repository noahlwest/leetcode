class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        cache = set()
        types = 0
        for num in candyType:
            if num not in cache:
                cache.add(num)
                types += 1
                
        n = len(candyType)
        
        return min(types, int(n/2))

#runtime: O(n)
#memory: O(n)
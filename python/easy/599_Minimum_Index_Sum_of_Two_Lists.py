class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        cache = {}
        for i in range(0, len(list1)):
            cache.update({list1[i] : i})
            
        min_sum = 2001
        ret = []
        for i in range(0, len(list2)):
            pref_sum = cache.get(list2[i], 2002) + i
            if pref_sum < min_sum:
                min_sum = pref_sum
                ret = [list2[i]]
            elif pref_sum == min_sum:
                ret.append(list2[i])
            
        return ret

#runtime: O(n + m)
#memory: O(n)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stash = {}
        for num in nums1:
            if num in stash:
                stash.update({num : stash[num]+1})
            else:
                stash.update({num : 1})
        
        ret = []
        for num in nums2:
            if num in stash:
                if stash[num] > 0:
                    stash.update({num : stash[num]-1})
                    ret.append(num)
        
        return ret

#runtime: O(n + m)
#memory: O(n)
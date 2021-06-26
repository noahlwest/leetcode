class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set()
        for num in nums1:
            nums1_set.add(num)
        
        ret_set = set()
        for num in nums2:
            if num in nums1_set:
                ret_set.add(num)
                
        return list(ret_set)

#runtime: O(n + m)
#memory: O(n + m)
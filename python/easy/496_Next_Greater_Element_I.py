class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = {}
        for i in range(0, len(nums2)):
            cache.update({nums2[i] : i})
            
        ret = []
            
        for num in nums1:
            index2 = cache[num]
            greater = -1
            while greater == -1 and index2 < len(nums2):
                if nums2[index2] > num:
                    greater = nums2[index2]
                index2 += 1
            ret.append(greater)
            
        return ret
                
#runtime: O(2n) -> O(n)
#memory: O(2n) -> O(n)
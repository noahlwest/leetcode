class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        #main idea: fill in from the back
        #three pointers:
        #current place in nums1
        #current place in nums2
        #index to replace in nums1
        
        #edge case: nums1 is an "empty" array
        empty_array = True
        for num in nums1:
            if num != 0:
                empty_array = False
                break
        
        if empty_array:
            for i in range(0, len(nums2)):
                nums1[i] = nums2[i]
                
            
        
        #replacements start at end of ret array (nums1)
        replace = len(nums1)-1
        #start at end of original numbers in num1
        index1 = m-1
        #start at the end of nums2
        index2 = n-1
        
        while(replace >= 0):
            #if we're still working with both lists
            if(replace == 2):
                print("index1: %d index2: %d" % (index1, index2))
                print("nums1: %d nums2: %d " % (nums1[index1], nums2[index2]))
            if index1 >= 0 and index2 >= 0:
                if nums1[index1] > nums2[index2]:
                    nums1[replace] = nums1[index1]
                    index1 -= 1
                    replace -= 1
                else:
                    nums1[replace] = nums2[index2]
                    index2 -= 1
                    replace -= 1
            elif index2 >= 0:
                #we're off nums1 "real number" boundary , but still have stuff in nums2
                nums1[replace] = nums2[index2]
                index2 -= 1
                replace -= 1
            else:
                #we're off nums2 boundary, and nums1 "earlier" nums are already sorted
                break
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #use a counter to keep track of current index
        #if current value > current index value
            #increment index
        
        if not bool(nums):
            return 0
        
        index_counter = 1
        
        for value in nums:
            if value > nums[index_counter-1]:
                nums[index_counter] = value
                index_counter += 1
                
        return index_counter
            
#runtime: O(n)
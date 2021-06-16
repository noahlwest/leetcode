class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #keep track of total and maximum
        
        #for each entry in the array:
            #current = max(entry, entry + current)
            #max = max(current, max)
        
        current_val = max_val = nums[0]
        
        for i in range(1, len(nums)):
            current_val = max(nums[i], nums[i] + current_val)
            max_val = max(current_val, max_val)
            
        return max_val
        
#runtime: O(n)
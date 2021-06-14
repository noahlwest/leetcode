class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #use a counter to keep track of current index
        #if current value is the target value:
            #do not advance the index counter
        #else
            #replace index counter value with current value
            #advance the index counter
        
        if not bool(nums):
            return 0
        
        index_counter = 0
        
        for value in nums:
            if value != val:
                nums[index_counter] = value
                index_counter += 1
                
        return index_counter

#runtime: O(n)
            
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        curr_num = nums[0]
        curr_amt = 1
        
        replace_index = 1
        search_index = 1
        while search_index < len(nums):
            if nums[search_index] > curr_num:
                curr_num = nums[search_index]
                nums[replace_index] = nums[search_index]
                replace_index += 1
                curr_amt = 1
            elif nums[search_index] == curr_num:
                curr_amt += 1
                if curr_amt <= 2:
                    nums[replace_index] = nums[search_index]
                    replace_index += 1
            search_index += 1
            
        return replace_index

    #runtime: O(n)
    #memory: O(1)
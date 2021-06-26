class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        find_zero = 0
        find_non_zero = 0
        zero_found = (nums[find_zero] == 0)
        while find_zero < len(nums) and find_non_zero < len(nums):
            if zero_found == True:
                #zero awaiting swap, find a non-zero to replace it with
                if nums[find_non_zero] != 0:
                    nums[find_zero], nums[find_non_zero] = nums[find_non_zero], nums[find_zero]
                    zero_found = False
                find_non_zero += 1
            else:
                #zero not awaiting swap, so find a zero to swap
                if nums[find_zero] == 0:
                    zero_found = True
                    find_non_zero = find_zero + 1
                else:
                    find_zero += 1
                    
#runtime: O(n)
#memory: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #at each step, pick the one that can jump the furthest

        i = 0
        while i+nums[i] < len(nums)-1:
            start_i = i
            if nums[i] == 0:
                return False
            if nums[i] == 1:
                i += 1
            else:
                start = i
                end = i+nums[i]
                for j in range(start, end):
                    if j+nums[j] > i+nums[i] and nums[j] != 0:
                        i = j
            if start_i == i:
                i += nums[i]
                
                
            
        return True
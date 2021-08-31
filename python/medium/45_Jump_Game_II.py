class Solution:
    def jump(self, nums: List[int]) -> int:
        
        #start at the end and pick the furthest back possible
        
        i = len(nums)-1
        jumps = 0
        while i > 0:
            dist = 0
            new_i = i
            for j in range(i, -1, -1):
                if nums[j] >= dist:
                    new_i = j
                dist += 1
            i = new_i
            jumps += 1
        
        return jumps
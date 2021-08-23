class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        closest = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    curr = nums[i] + nums[j] + nums[k]
                    if curr == target:
                        return curr
                    if abs(target - curr) < abs(target - closest):
                        closest = curr
                    
        return closest

#runtime: O(n^3)
#memory: O(1)
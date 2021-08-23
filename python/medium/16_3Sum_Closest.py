class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort() #n log n
        ret = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == target:
                    return target
                if abs(target - curr) < abs(target - ret):
                    ret = curr
                if curr < target:
                    j += 1
                elif curr > target:
                    k -= 1
                    
        return ret

#runtime: O(n^2)
#memory: O(1)
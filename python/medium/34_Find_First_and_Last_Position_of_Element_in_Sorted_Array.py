class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0:
            return [-1, -1]
        
        left = 0
        right = len(nums)-1
        middle = 0
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                break
            elif nums[middle] < target:
                left = middle+1
            elif nums[middle] > target:
                right = middle-1
                
        if nums[middle] != target:
            return [-1, -1]
        
        left, right = middle, middle
        
        found = True
        while left > 0 and found == True:
            found = False
            if nums[left-1] == target:
                left = left-1
                found = True
        
        found = True
        while right < len(nums)-1 and found == True:
            found = False
            if nums[right+1] == target:
                right = right+1
                found = True
                
        return [left, right]
                
        
#runtime: O(n)
#memory: O(1)
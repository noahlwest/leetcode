class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        middle = (left+right)//2
        
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        
        while True:
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                if nums[middle-1] < target:
                    return middle
                right = middle
                middle = (left+right)//2
            elif nums[middle] < target:
                if nums[middle+1] > target:
                    return middle+1
                left = middle
                middle = (left+right)//2
                
#runtime: O(log n)
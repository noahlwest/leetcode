class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        max_area = 0
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area
            #if left is smaller, move left pointer inwards
            if height[left] < height[right]:
                left += 1
            #if right is smaller or equal move right pointer inwards
            else:
                right -= 1
                
        return max_area
                
#runtime: O(n)
#memory: O(1)
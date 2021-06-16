class Solution:
    def mySqrt(self, x: int) -> int:
        
        #binary search the numbers to find the int(floor(sqrt(x)))
        
        left = 0
        right = 46341
        middle = (left + right)//2
        
        while True:
            mid_val = middle * middle
            if mid_val < x:
                if (middle+1) * (middle+1) > x:
                    return middle
                left = middle + 1
                middle = (left + right)//2
            elif mid_val > x:
                right = middle - 1
                middle = (left + right)//2
            else: #mid_val == x:
                return middle

#runtime: O(1) (logarithmic, way faster than the brute force solution)
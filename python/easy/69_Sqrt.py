class Solution:
    def mySqrt(self, x: int) -> int:
        
        #try each number up until around sqrt(2^31)
        
        closest_distance = 1000000
        closest_int = 0
        
        for i in range(0, 46341):                
            distance = x - (i * i)
            if distance < closest_distance and i*i <= x:
                closest_int = i
                closest_distance = distance
                
        return closest_int

#runtime O(1) (but it's still not good)
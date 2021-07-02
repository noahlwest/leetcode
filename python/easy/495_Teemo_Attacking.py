class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        ret = 0
        last_time = timeSeries[0]
        for time in timeSeries:
            if time - last_time > duration:
                last_time = time
                ret += duration
            else:
                ret += time - last_time
                last_time = time
        
        return ret + duration

#runtime: O(n)
#memory: O(1)
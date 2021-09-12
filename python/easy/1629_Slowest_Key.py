class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        max_time = releaseTimes[0]
        max_key = keysPressed[0]
        
        for i in range(1, len(keysPressed)):
            time = releaseTimes[i] - releaseTimes[i-1]
            if time > max_time or (time == max_time and keysPressed[i] > max_key):
                max_time = time
                max_key = keysPressed[i]
        
        return max_key

    #runtime: O(n)
    #memory: O(1)
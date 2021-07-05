class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        average = 0
        for i in range(0, k):
            average += (nums[i]/k)
        
        max_sum = average
            
        for i in range(k, len(nums)):
            average -= (nums[i-k]/k)
            average += (nums[i]/k)
            max_sum = max(average, max_sum)
            
        return max_sum

#runtime: O(n)
#memory: O(1)
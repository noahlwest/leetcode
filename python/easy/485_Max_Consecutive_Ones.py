class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec = 0
        consec = 0
        for num in nums:
            if num == 0:
                max_consec = max(max_consec, consec)
                consec = 0
            else:
                consec += 1
        return max(max_consec, consec)

#runtime: O(n)
#memory: O(1)
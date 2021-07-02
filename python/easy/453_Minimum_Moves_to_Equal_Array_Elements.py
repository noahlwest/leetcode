class Solution:
    def minMoves(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        arr_sum = sum(nums)
        arr_min = min(nums)
        
        moves = arr_sum - (arr_min * length)
                
        return moves    

#runtime: O(n)
#memory: O(1)
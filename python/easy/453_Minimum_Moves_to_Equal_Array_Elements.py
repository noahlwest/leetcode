class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #if (sum / length) == max: all elements are equal
        arr_sum = sum(nums)
        length = len(nums)
        arr_max = max(nums)
        moves = 0
        
        while arr_sum / length != arr_max:
            #print(arr_sum, length, arr_max)
            if arr_sum / length > arr_max:
                arr_max += 1
                arr_sum += length-1
            elif arr_sum / length < arr_max:
                arr_sum += length-1
            moves += 1
                
        return moves    

#runtime: scales with (max - min) O(1) I guess, since -10^9 <= min, max <= 10^9
#memory: O(1)
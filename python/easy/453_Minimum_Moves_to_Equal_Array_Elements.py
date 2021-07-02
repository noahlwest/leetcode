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

#runtime: O(n) due to sum(), but really scales with (max-min)
#memory: O(1)
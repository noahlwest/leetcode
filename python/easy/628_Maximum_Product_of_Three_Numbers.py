class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #get the 3 maximum values
        #get the two minimum + maximum
        first_max = -1001
        second_max = -1001
        third_max = -1001
        first_min = 1001
        second_min = 1001
        
        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max:
                third_max = second_max
                second_max = num
            elif num > third_max:
                third_max = num
                
            if num < first_min:
                second_min = first_min
                first_min = num
            elif num < second_min:
                second_min = num

        return max((first_max * first_min * second_min), (first_max * second_max * third_max))

#runtime: O(n)
#memory: O(1)
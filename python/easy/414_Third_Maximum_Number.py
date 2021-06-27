class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = None
        second_max = None
        third_max = None
        
        for num in nums:
            if first_max is None:
                first_max = num
            elif second_max is None:
                if num != first_max:
                    if num < first_max:
                        second_max = num
                    else:
                        second_max = first_max
                        first_max = num
            elif third_max is None:
                if num != first_max and num != second_max:
                    if num < second_max:
                        third_max = num
                    elif num > second_max and num < first_max:
                        third_max = second_max
                        second_max = num
                    elif num > first_max:
                        third_max = second_max
                        second_max = first_max
                        first_max = num
            else:
                if num == first_max or num == second_max or num == third_max:
                    continue
                if num > first_max:
                    third_max = second_max
                    second_max = first_max
                    first_max = num
                elif num < first_max and num > second_max:
                    third_max = second_max
                    second_max = num
                elif num < second_max and num > third_max:
                    third_max = num
                else:
                    pass
        
        if third_max is not None:
            return third_max
        else:
            return first_max
#runtime: O(n)
#memory: O(1)
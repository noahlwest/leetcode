class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 0:
            return []
        
        first_in_range = nums[0]
        last_in_range = nums[0]
        ret = []
        broken_sequence = False
        
        for i in range(1, len(nums)):
            if nums[i] == last_in_range + 1:
                last_in_range = nums[i]
            else:
                if first_in_range == last_in_range:
                    cur_range = str(first_in_range)
                else:
                    cur_range = str(first_in_range) + "->" + str(last_in_range)
                ret.append(cur_range)
                first_in_range = nums[i]
                last_in_range = nums[i]
        #add final range to ret
        if first_in_range == last_in_range:
            cur_range = str(first_in_range)
        else:
            cur_range = str(first_in_range) + "->" + str(last_in_range)
        ret.append(cur_range)
                
        return ret
            
#runtime: O(n)
#memory: O(n)
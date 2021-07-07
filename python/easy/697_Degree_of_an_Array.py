class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        count = [0] * 50000
        first_index = [-1] * 50000
        max_dict = {}
        max_amount = 0
        
        for i in range(len(nums)):
            count[nums[i]] += 1
            
            if count[nums[i]] > max_amount:
                max_amount = count[nums[i]]
                max_dict.clear()
                max_dict.update({nums[i] : i})
            elif count[nums[i]] == max_amount:
                max_dict.update({nums[i] : i})    
            
            if first_index[nums[i]] == -1:
                first_index[nums[i]] = i
                
        
        ret_min = 50000
        for number, last_index in max_dict.items():
            ret_min = min(last_index - first_index[number], ret_min)
        
        return 1 + ret_min

#runtime: O(n) (really O(1) since the problem gives an upper bound)
#memory: O(n) (really O(1) since the problem gives an upper bound)
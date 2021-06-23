class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #NOT memory efficient like the XOR solution
        #but real people will not remember XOR properties can solve this problem.
        #however, does not require the extra final traversal of the hashmap that is common
        
        seen = {}
        sum = 0
        
        for num in nums:
            if num in seen:
                sum -= num
            else:
                seen.update({num:1})
                sum += num
                
        return sum
        
#runtime: O(n) (dict lookup is O(1) on average)
#memory: O(n) (constant memory with XOR implementation, but less readable/understandable)
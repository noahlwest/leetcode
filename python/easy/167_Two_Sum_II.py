class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #non-optimal solution:
        #put every seen number into a dictionary
        #for every item:
            #if target - current_num in seen:
                #return [seen[i], seen[current_num]]
            
        seen = {}
        
        for i in range(0, len(numbers)):
            if target - numbers[i] in seen:
                if i != seen[target - numbers[i]]:
                    return [min(i+1, seen[target - numbers[i]]+1), max(i+1, seen[target - numbers[i]]+1)]
            
            if numbers[i] not in seen:
                seen.update({numbers[i] : i})
#runtime: O(n)
#memory: O(n)
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #edge cases
        if len(arr) < 3:
            return False
        if arr[1] < arr[0]:
            return False
        
        i = 1
        increasing = True
        decreasing = False
        while i < len(arr):
            if arr[i] == arr[i-1]:
                return False
            if increasing == True:
                if arr[i] < arr[i-1]:
                    increasing = False
                    decreasing = True
                else:
                    pass
            elif decreasing == True:
                if arr[i] > arr[i-1]:
                    return False
            i += 1
                
        return decreasing

#runtime: O(n)
#memory: O(1)
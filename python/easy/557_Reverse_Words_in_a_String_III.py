class Solution:
    def reverseWords(self, s: str) -> str:
        
        left = 0
        right = 0
        slist = list(s)
        
        for i in range(0, len(slist)):
            if slist[i] != " ":
                right += 1
            else:
                right -= 1
                while left < right:
                    slist[left], slist[right] = slist[right], slist[left]
                    left += 1
                    right -= 1
                left = i+1
                right = i+1
        right -= 1
        if slist[len(slist)-1] != " ":
            while left < right:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
        
                
        return "".join(slist)
            
#runtime: O(n)
#memory: O(n)
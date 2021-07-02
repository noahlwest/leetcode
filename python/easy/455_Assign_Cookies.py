class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #sort both arrays and step through them
        g.sort()
        s.sort()
        
        g_index = 0
        s_index = 0
        
        while g_index < len(g) and s_index < len(s):
            g_val = g[g_index]
            s_val = 0
            while s_val < g_val and s_index < len(s):
                s_val = s[s_index]
                s_index += 1
                
            if s_val < g_val:
                break
                
            g_index += 1
                
        return g_index
                
#runtime: O(n log n + m log m) due to the sorting
#memory: O(1)
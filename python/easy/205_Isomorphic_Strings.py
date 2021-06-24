class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_cache = {}
        t_cache = {}
        s_counter = 0
        t_counter = 0
        
        for i in range(0, len(s)):
            #only valid scenarios:
            #if both are in the cache and have the same pattern value
                #continue
            #if neither are in the cache
                #continue
            #else: not a valid scenario
                #return false
                
            if (s[i] in s_cache and t[i] in t_cache):
                #if they don't have the same pattern value
                if s_cache[s[i]] != t_cache[t[i]]:
                    return False
                pass
            elif (s[i] not in s_cache and t[i] not in t_cache):
                s_counter += 1
                t_counter += 1
                s_cache.update({s[i] : s_counter})
                t_cache.update({t[i] : t_counter})
            else: #one is in, one is out
                return False
            
        return True

#runtime: O(n)
#memory: O(2n) = O(n)
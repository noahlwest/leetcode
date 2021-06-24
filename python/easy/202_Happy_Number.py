class Solution:
    def isHappy(self, n: int) -> bool:
        
        cache = {}
        
        while True:
            val_str = str(n)
            cur_sum = 0
            for char in val_str:
                cur_sum += int(char)**2
            if cur_sum == 1:
                return True
            if cur_sum in cache:
                return False
            else:
                cache.update({cur_sum : "_"})
            n = str(cur_sum)

#runtime: really not sure. First iteration gets bigger for each power of 10 in the initial number.
          #otherwise, I don't know how to analyze this.
#memory: same case as runtime. Not sure what determines how many iterations each run goes through.
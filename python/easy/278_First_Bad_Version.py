# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #if n == 1:
        #    return 1
        
        #binsearch
        left = 1
        right = n
        middle = (left + right)//2
        while left < right:
            if isBadVersion(middle):
                right = middle
                middle = (left+right)//2
            else:
                left = middle+1
                middle = (left+right)//2
                
        return left

#runtime (calls to API): O(log n)
#memory: O(1)
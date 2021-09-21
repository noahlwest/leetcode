class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rows = len(accounts)
        columns = len(accounts[0])
        ret = [0]*rows
        for i in range(0, rows):
            for j in range(0, columns):
                ret[i] += accounts[i][j]
        return max(ret)

#runtime: O(n*m)
#memory: O(n)
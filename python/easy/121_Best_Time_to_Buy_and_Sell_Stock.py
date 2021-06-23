class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum_price = 10001
        profit = 0
        
        for price in prices:
            if price < minimum_price:
                minimum_price = price
            if price - minimum_price > profit:
                profit = price - minimum_price
                
        return profit
            
#runtime: O(n)
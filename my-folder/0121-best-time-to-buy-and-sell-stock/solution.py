class Solution(object):
    def maxProfit(self, prices):
        current_lowest = prices[0]
        current_max_profit = 0
        for price in prices:
            if price < current_lowest:
                current_lowest = price
            elif price - current_lowest > current_max_profit:
                current_max_profit = price - current_lowest
        return current_max_profit
            
        

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_lowest = prices[0]
        max_profits = 0
        for price in prices:
            if price < current_lowest:
                current_lowest = price
            else:
                if price - current_lowest > max_profits:
                    max_profits = price - current_lowest
        return max_profits

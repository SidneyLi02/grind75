class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # O(n) time, O(1) space optimal 2 pointer sol
        if len(prices) <= 1: # unneeded check, for readability only
            return 0
        else:
            buy, sell = 0, 1
            max_profit = 0
            while sell < len(prices):
                if prices[buy] < prices[sell]:
                    curr_profit = prices[sell] - prices[buy]
                    max_profit = max(max_profit, curr_profit)
                else:
                    buy = sell
                sell += 1
        return max_profit
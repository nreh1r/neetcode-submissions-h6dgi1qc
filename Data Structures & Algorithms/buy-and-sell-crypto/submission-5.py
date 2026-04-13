class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r, = 0, 1

        while r < len(prices):
            new_profit = prices[r] - prices[l]
            if new_profit < 0:
                l = r
            profit = max(profit, new_profit)
            r += 1
        return profit
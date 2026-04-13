class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r, = 0, 1

        while r < len(prices):
            while r < len(prices):
                new_profit = prices[r] - prices[l]
                print(f"new profit: {new_profit}")
                print(f"left: {l}, right: {r}")
                if new_profit < 0:
                    l = r
                    break
                profit = max(profit, new_profit)
                r += 1
            r += 1
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            print(l, r)
            print(prices[l], prices[r])
            if prices[l] > prices[r]:
                print("here")
                l = r
                r += 1
                continue
            
            profit = max(profit, prices[r] - prices[l])
            r += 1
        
        return profit
            
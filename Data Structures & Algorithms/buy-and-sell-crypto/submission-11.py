class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = prices[0]

        for i in range(len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]
            
            profit = max(profit, prices[i] - minBuy)
        
        return profit
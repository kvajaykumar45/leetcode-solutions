class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            diff = prices[i] - minPrice
            if diff > maxPro:
                maxPro = diff
        return maxPro

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        discounts = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack!=[] and stack[-1] > prices[i]:
                stack.pop()
            if stack!=[]:
                discounts[i] = prices[i] - stack[-1]
            else:
                discounts[i] = prices[i]
            stack.append(prices[i])

        return discounts
        

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i, buy, sell, profit = 0, 0, 0, 0
        while i < n - 1:
            while i < n and prices[i + 1] <= prices[i]:
                i += 1
                if i == n - 1:
                    break
            if i == n - 1:
                break

            buy = prices[i]

            while i < n and prices[i + 1] > prices[i]:
                i += 1
                if i == n - 1:
                    break

            sell = prices[i]

            profit += sell - buy
        
        return profit


prices = list(map(int, input().split(" ")))
max_profit = Solution()
print(max_profit.maxProfit(prices))

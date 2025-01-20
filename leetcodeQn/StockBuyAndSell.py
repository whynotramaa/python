class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            cost = prices[i]-mini
            profit = max(profit,cost)
            mini = min(mini,prices[i])
        return profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         mini, profit = float('inf'), 0
#         for price in prices:
#             mini = min(mini, price)  # Update minimum price so far
#             profit = max(profit, price - mini)  # Update max profit
#         return profit

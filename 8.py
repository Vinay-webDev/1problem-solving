"""121. Best Time to Buy and Sell Stock"""
prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
class Solution:
    def maxProfit(self, prices):
        l, r = 0, 1
        max_profit = 0
        while r != len(prices):
            if prices[l] < prices[r]:
                current_max_profit = prices[r] - prices[l]
                max_profit = max(max_profit, current_max_profit)
            else:
                l = r
            r = r + 1
        return max_profit
sol = Solution()
print(sol.maxProfit(prices1))  #5
print(sol.maxProfit(prices2))  #0

""""from LeetCode best solutions"""
class Solution:
    def maxProfitBest(self, prices):
        if not prices: 
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit




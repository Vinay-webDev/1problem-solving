"""121. Best Time to Buy and Sell Stock"""
prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
class Solution:
    def maxProfit(self, prices):
        l = 0
        r = len(prices) - 1
        max_profit = 0
        while l < r:
            current_max_profit = abs(prices[l] - prices[r])
            max_profit = max(max_profit, current_max_profit)
            if prices[l] < prices[r]:
                l = l + 1
            else:
                r = r - 1
        return max_profit
sol = Solution()
print(sol.maxProfit(prices1))  #6

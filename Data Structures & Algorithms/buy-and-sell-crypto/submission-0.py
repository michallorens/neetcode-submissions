class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        window_len = len(prices)

        while window_len > 1:
            for start_day in range(len(prices) - window_len + 1):
                profit = prices[start_day + window_len - 1] - prices[start_day]

                if profit > max_profit:
                    max_profit = profit

            window_len -= 1

        return max_profit
func maxProfit(prices []int) int {
	max_profit := 0
	buy_price := prices[0]

	for i := 1; i < len(prices); i++ {
		max_profit = max(max_profit, prices[i] - buy_price)
		buy_price = min(buy_price, prices[i])
	}

	return max_profit
}

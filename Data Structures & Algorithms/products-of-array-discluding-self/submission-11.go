func productExceptSelf(nums []int) []int {
	product := 1
	products := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		products[i] = product
		product = nums[i] * product
	}

	product = 1

	for i := len(nums) - 1; i >= 0; i-- {
		products[i] *= product
		product = nums[i] * product
	}

	return products
}

func maxArea(heights []int) int {
	max_area := 0
	left := 0
	right := len(heights) - 1

	for left < right {
		area := min(heights[left], heights[right]) * (right - left)
		max_area = max(max_area, area)

		if heights[left] < heights[right] {
			left++
		} else {
			right--
		}
	}

	return max_area
}

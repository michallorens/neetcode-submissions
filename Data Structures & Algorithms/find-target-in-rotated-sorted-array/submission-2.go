func search(nums []int, target int) int {
	i := 0
	left := 0
	right := len(nums) - 1

	for left <= right {
		i = (left + right) / 2

		if nums[i] > nums[right] {
			left = i + 1
		} else if nums[i] < nums[left]  {
			right = i
		} else {
			right = i - 1
		}
	}
	
	left = 0

	for left <= right {
		j := (left + right) / 2

		if nums[j] < target {
			left = j + 1
		} else if nums[j] > target {
			right = j - 1
		} else if nums[j] == target {
			return j
		}
	}

	left = i
	right = len(nums) - 1

	for left <= right {
		j := (left + right) / 2

		if nums[j] < target {
			left = j + 1
		} else if nums[j] > target {
			right = j - 1
		} else if nums[j] == target {
			return j
		}
	}

	return -1
}

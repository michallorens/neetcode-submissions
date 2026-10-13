func twoSum(nums []int, target int) []int {
    diffs := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		j, ok := diffs[nums[i]]

		if ok {
			return []int{j, i}
		} else {
			diffs[target - nums[i]] = i
		}
	}

	return []int{0,0}
}

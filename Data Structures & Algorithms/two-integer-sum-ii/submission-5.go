func twoSum(numbers []int, target int) []int {
	diffs := make(map[int]int, len(numbers) / 2 + 1)

	for i, n := range numbers {
		if j, ok := diffs[n]; ok {
			return []int{j+1, i+1}
		} else {
			diffs[target - n] = i
		}
	}

	return nil
}

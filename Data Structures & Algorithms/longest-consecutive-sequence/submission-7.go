

func longestConsecutive(nums []int) int {
	hashset := make(map[int]bool, len(nums))
	longest := 0

	for _, n := range nums {
		hashset[n] = true
	}

	for n, _ := range hashset {
		if _, ok := hashset[n-1]; ok {
			continue
		}

		m := n + 1
		
		for {
			if _, ok := hashset[m]; !ok {
				break
			}
			
			m++
		}

		longest = max(m - n, longest)
	}

	return longest
}

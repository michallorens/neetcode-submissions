

func longestConsecutive(nums []int) int {
	hashset := make(map[int]bool, len(nums))
	longest_sequence := 0

	for _, n := range nums {
		hashset[n] = true
	}

	for n, _ := range hashset {
		_, ok := hashset[n-1]

		if ok {
			continue
		} else {
			m := n + 1
			
			for {
				_, ok := hashset[m]

				if ok {
					m++
				} else {
					break
				}
			}

			longest_sequence = max(m - n, longest_sequence)
		}
	}

	return longest_sequence
}

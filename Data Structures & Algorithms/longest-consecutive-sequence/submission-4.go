

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
			sequence_len := 1
			m := n + 1
			
			for {
				_, ok := hashset[m]

				if ok {
					sequence_len++
					m++
				} else {
					break
				}
			}

			if sequence_len > longest_sequence {
				longest_sequence = sequence_len
			}
		}
	}

	return longest_sequence
}

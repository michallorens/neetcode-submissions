func lengthOfLongestSubstring(s string) int {
	left := 0
	longest := 0
	chars := make(map[rune]bool)

	for i := 0; i < len(s); i++ {
		c := rune(s[i])

		for chars[c] {
			delete(chars, rune(s[left]))
			left++
		}

		chars[c] = true
		longest = max(longest, i - left + 1)
	}

	return longest
}

func characterReplacement(s string, k int) int {
	char_freq := make(map[rune]int)
	result := 0
	top_char := rune(s[0])
	window := 0

	for i := 0; i < len(s); i++ {
		c := rune(s[i])
		char_freq[c]++
		window++

		if char_freq[c] >= char_freq[top_char] {
			top_char = c
		}

		if window > char_freq[top_char] + k {
			char_freq[rune(s[i - window + 1])]--
			window--
		}

		result = max(result, window)
	}

	return result
}

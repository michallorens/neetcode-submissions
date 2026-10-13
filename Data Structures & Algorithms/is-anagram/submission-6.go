func isAnagram(s string, t string) bool {
	var chars map[rune]int16 = make(map[rune]int16)

	if len(s) != len(t) {
		return false
	}

	for i := 0; i < len(s); i++ {
		chars[rune(s[i])]++
		chars[rune(t[i])]--
	}

	for i := 0; i < len(s); i++ {
		if chars[rune(s[i])] != 0 {
			return false
		}
	}

	return true
}

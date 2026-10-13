func isAnagram(s string, t string) bool {
	var chars map[rune]int16 = make(map[rune]int16)

	if len(s) != len(t) {
		return false
	}

	for i := 0; i < len(s); i++ {
		_, ok := chars[rune(s[i])]

		if ok {
			chars[rune(s[i])] += 1
		} else {
			chars[rune(s[i])] = 1
		}
	}

	for i := 0; i < len(t); i++ {
		_, ok := chars[rune(t[i])]

		if ok {
			chars[rune(t[i])] -= 1
		} else {
			return false
		}
	}

	for i := 0; i < len(s); i++ {
		if chars[rune(s[i])] != 0 {
			return false
		}
	}

	return true
}

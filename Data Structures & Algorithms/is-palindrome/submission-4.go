func isAlphaNumeric(r rune) bool {
	return (r >= 'A' && r <= 'z') || (r >= '0' && r <= '9')
}

func isPalindrome(s string) bool {
	left := 0
	right := len(s) - 1

	for left < right {
		l := unicode.ToLower(rune(s[left]))
		r := unicode.ToLower(rune(s[right]))

		if !isAlphaNumeric(l) {
			left++
		} else if !isAlphaNumeric(r) {
			right--
		} else if l == r {
			left++
			right--
		} else {
			return false
		}
	}

	return true
}

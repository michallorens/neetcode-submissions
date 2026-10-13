func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	var chars [26]int8

	for i := 0; i < len(s); i++ {
		chars[s[i]-'a']++
		chars[t[i]-'a']--
	}

	for _, count := range chars {
		if count != 0 {
			return false
		}
	}

	return true
}

func checkInclusion(s1 string, s2 string) bool {
	var letters1 [26]int
	var letters2 [26]int

	for i := 0; i < len(s1); i++ {
		letters1[s1[i] - 'a']++
	}

	for i := 0; i < len(s2); i++ {
		letters2[s2[i] - 'a']++

		if i > len(s1) - 1 {
			letters2[s2[i - len(s1)] - 'a']--
		}

		if letters1 == letters2 {
			return true
		}
	}

	return false
}

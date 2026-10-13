import "slices"

func sortLetters(str string) string {
	runes := []rune(str)
	slices.Sort(runes)
	return string(runes)
}

func groupAnagrams(strs []string) [][]string {
	groups := make(map[string][]string)

	for _, s := range strs {
		key := sortLetters(s)
		groups[key] = append(groups[key], s)
	}

	var values [][]string

	for _, v := range groups {
		values = append(values, v)
	}

	return values
}

type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	var b strings.Builder

	for _, s := range strs {
		b.WriteString(s)
		b.WriteString(string(rune(257)))
	}

	return b.String()
}

func (s *Solution) Decode(encoded string) []string {
	if encoded == "" {
		return []string{}
	}

	return strings.Split(encoded[:len(encoded)-len(string(rune(257)))], string(rune(257)))
}

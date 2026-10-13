type Solution struct{}

var delimiter string = string(rune(257))

func (s *Solution) Encode(strs []string) string {
	var b strings.Builder

	for _, s := range strs {
		b.WriteString(s)
		b.WriteString(delimiter)
	}

	return b.String()
}

func (s *Solution) Decode(encoded string) []string {
	if encoded == "" {
		return []string{}
	}

	encoded = strings.TrimSuffix(encoded, delimiter)
	return strings.Split(encoded, delimiter)
}

func topKFrequent(nums []int, k int) []int {
	seen := make(map[int]int, len(nums))
	buckets := make([][]int, len(nums))
	
	for _, n := range nums {
		seen[n]++
	}

	for n, count := range seen {
		buckets[count-1] = append(buckets[count-1], n)
	}

	i, result := len(nums)-1, make([]int, 0, k)
	
	for len(result) < k {
		result = append(result, buckets[i]...)
		i--
	}

	return result[:k]
}

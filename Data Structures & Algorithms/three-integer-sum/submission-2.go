import "slices"

func threeSum(nums []int) [][]int {
	slices.Sort(nums)
	triplets := make([][]int, 0)

	for i := 0; i < len(nums) - 2; i++ {
		left, right := i + 1, len(nums) - 1

		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		for left < right {
			sum := nums[i] + nums[left] + nums[right]
			
			if sum > 0 {
				right--
			} else if sum < 0 {
				left++
			} else {
				triplet := []int{nums[i],nums[left],nums[right]}
				triplets = append(triplets, triplet)
				left++
				right--
				for left < right && nums[left] == nums[left-1] {
					left++
				}
				for left < right && nums[right] == nums[right+1] {
					right--
				}
			}
		}
	}

	return triplets
}

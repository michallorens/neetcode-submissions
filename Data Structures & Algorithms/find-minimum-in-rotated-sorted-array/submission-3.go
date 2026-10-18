func findMin(nums []int) int {
    left := 0
    right := len(nums) - 1

    for left < right {
        i := (left + right) / 2

        if nums[i] > nums[right] {
            left = i + 1
        } else if nums[i] < nums[left] {
            right = i
        } else {
            right = i - 1
        }
    }

    return nums[left]
}

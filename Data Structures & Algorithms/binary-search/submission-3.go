func search(nums []int, target int) int {
    left := 0
    right := len(nums) - 1

    for left <= right {
        i := (left + right) / 2

        if nums[i] < target {
            left = i + 1
        } else if nums[i] > target {
            right = i - 1
        } else {
            return i
        }
    }

    return -1
}

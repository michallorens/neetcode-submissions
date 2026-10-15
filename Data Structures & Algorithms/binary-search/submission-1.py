class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while end >= start:
            i = (end + start) // 2

            if nums[i] > target:
                end = i - 1
            elif nums[i] < target:
                start = i + 1
            else:
                return i

        return -1
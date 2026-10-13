class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        nums_len = len(nums)

        if nums_len < 2:
            return False

        for i in range(nums_len-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True

        return False
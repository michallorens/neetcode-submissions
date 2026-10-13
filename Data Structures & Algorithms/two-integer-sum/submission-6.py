class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexes.keys() and indexes[diff] != i:
                return sorted([i, indexes[diff]])
            else:
                indexes[nums[i]] = i

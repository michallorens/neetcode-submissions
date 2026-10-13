class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i in range(len(nums)):
            if target - nums[i] in indexes.keys() and indexes[target - nums[i]] != i:
                return sorted([i, indexes[target - nums[i]]])
            else:
                indexes[nums[i]] = i

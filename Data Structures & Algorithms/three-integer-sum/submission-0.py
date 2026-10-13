class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        left = 0
        triplets = []

        while left < len(nums) - 2:
            if nums[left] > 0:
                break
            if left > 0 and nums[left] == nums[left - 1]:
                left += 1
                continue

            mid = left + 1
            right = len(nums) - 1

            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total == 0:
                    triplets.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    mid += 1
                else:
                    right -= 1

            left += 1

        return triplets
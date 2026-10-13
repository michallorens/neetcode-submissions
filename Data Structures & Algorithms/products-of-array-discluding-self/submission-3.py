class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        prefixes = []
        suffixes = []
        length = len(nums)

        for i in range(length):
            prefixes.append(prefix)
            suffixes.append(suffix)
            prefix = prefix * nums[i]
            suffix = suffix * nums[-i-1]

        for i in range(length):
            prefixes[i] = prefixes[i] * suffixes[-i-1]

        return prefixes
        

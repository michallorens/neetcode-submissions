class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        product = 1
        results = []

        for i in range(length):
            results.append(product)
            product = product * nums[i]

        product = 1

        for i in range(length - 1, -1, -1):
            results[i] = results[i] * product
            product = product * nums[i]

        return results
        

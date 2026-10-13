class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix_products = []

        for n in nums:
            prefix_products.append(product)
            product = product * n

        product = 1
        suffix_products = []

        for n in reversed(nums):
            suffix_products.append(product)
            product = product * n

        for i in range(len(prefix_products)):
            prefix_products[i] = prefix_products[i] * suffix_products[-1 * (i+1)]

        return prefix_products
        

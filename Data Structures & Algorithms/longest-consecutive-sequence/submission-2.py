class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        longest_k = 0
        current_k = 1
        prev_num = None

        for n in sorted_nums:
            if n - 1 == prev_num:
                current_k = current_k + 1
            elif n == prev_num:
                continue
            else:
                current_k = 1

            prev_num = n

            if current_k > longest_k:
                longest_k = current_k

        return longest_k

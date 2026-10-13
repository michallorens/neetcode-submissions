class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            max_height = max(max_height, (right - left) * min(heights[left], heights[right]))

            if heights[right] < heights[left]:
                right = right - 1
            else:
                left = left + 1

        return max_height

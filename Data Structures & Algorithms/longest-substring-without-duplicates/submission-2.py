
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        result = 0

        for right, char in enumerate(s):
            while char in chars:
                chars.remove(s[left])
                left += 1

            chars.add(char)
            result = max(result, right - left + 1)

        return result

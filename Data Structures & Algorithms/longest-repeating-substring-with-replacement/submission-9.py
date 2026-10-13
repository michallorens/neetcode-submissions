class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {c:0 for c in s}
        top_char = s[0]
        left = 0
        result = 0

        for right, char in enumerate(s):
            chars[char] += 1

            if chars[char] >= chars[top_char]:
                top_char = char

            while right - left + 1 - chars[top_char] > k:
                chars[s[left]] -= 1
                left += 1

                if chars[char] >= chars[top_char]:
                    top_char = char

            result = max(result, right - left + 1)

        return result
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in letters.keys():
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1

        for i in range(len(t)):
            if t[i] in letters.keys():
                letters[t[i]] -= 1
            else:
                return False

        for v in letters.values():
            if v != 0:
                return False

        return True
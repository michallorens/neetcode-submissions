class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for c in s1:
            s1_freq[ord(c)-ord("a")] += 1

        for i in range(len(s2)):
            c = s2[i]
            s2_freq[ord(c)-ord("a")] += 1

            if i >= len(s1):
                s2_freq[ord(s2[i - len(s1)])-ord("a")] -= 1

            if s1_freq == s2_freq:
                return True

        return False

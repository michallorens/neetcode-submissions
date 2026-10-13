class Solution:
    def isValid(self, s: str) -> bool:
        heap = []
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for c in s:
            if c in mapping.values():
                heap.append(c)
            elif not heap or mapping[c] != heap[-1]:
                return False
            else:
                heap.pop()

        return True if not heap else False

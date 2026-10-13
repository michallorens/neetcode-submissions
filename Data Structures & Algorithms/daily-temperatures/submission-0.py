class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        prev_t = None
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if not prev_t or t <= prev_t:
                stack.append((i, t))
            else:
                while stack and stack[-1][1] < t:
                    j, _ = stack.pop()
                    result[j] = i - j

                stack.append((i, t))

            prev_t = t

        return result

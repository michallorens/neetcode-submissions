class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for token in tokens:
            if token not in "+-*/":
                nums.append(int(token))
                continue

            right = nums.pop()
            left = nums.pop()

            if token == "+":
                nums.append(left + right)
            if token == "-":
                nums.append(left - right)
            if token == "*":
                nums.append(left * right)
            if token == "/":
                nums.append(int(left / right))

        return nums.pop()
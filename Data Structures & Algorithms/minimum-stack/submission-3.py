class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min:
            self.min.append(val)
            return

        curr_min = self.min[-1]

        if val < curr_min:
            self.min.append(val)
        else:
            self.min.append(curr_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]

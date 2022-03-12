class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_list = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # self.max_list.append([x,m])

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        max_value = self.peekMax()
        # max_index = self.stack.index(max_value)
        for max_index in range(len(self.stack)-1,-1,-1):
            if self.stack[max_index] == max_value:
                break
        self.stack = self.stack[:max_index] + self.stack[max_index+1:]
        return max_value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
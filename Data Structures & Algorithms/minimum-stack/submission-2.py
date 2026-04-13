class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        self._set_minimum_stack_value(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]
    
    def _set_minimum_stack_value(self, val: int) -> None:
        if not self.min_value:
            self.min_value.append(val)
        else:
            self.min_value.append(min(self.min_value[-1], val))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }

        self.stack = []

        for token in tokens:
            if token in operands:
                operands[token]()
            else:
                self.stack.append(int(token))
        
        return self.stack[0]
    
    def add(self):
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack.append(val1 + val2)
    
    def subtract(self):
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack.append(val2 - val1)

    def multiply(self):
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack.append(val1 * val2)
    
    def divide(self):
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        self.stack.append(int(val2 / val1))
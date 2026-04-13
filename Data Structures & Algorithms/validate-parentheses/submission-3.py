class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for p in s:
            if p not in paren_map:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if paren_map[p] != val:
                    return False
        return len(stack) == 0



class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        stack = []

        for p in s:
            if p not in paren_map:
                stack.append(p)
                continue
            elif not stack or stack[-1] != paren_map[p]:
                return False
            stack.pop()
        return not stack



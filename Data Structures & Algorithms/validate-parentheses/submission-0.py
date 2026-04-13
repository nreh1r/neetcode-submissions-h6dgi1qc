class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        stack = []
        for p in s:
            if p in paren_map.keys() and len(stack) == 0:
                return False
            elif p in paren_map.keys() and len(stack) > 0:
                prev_paren = stack.pop()
                if prev_paren != paren_map[p]:
                    return False
            else:
                stack.append(p)
        return len(stack) == 0



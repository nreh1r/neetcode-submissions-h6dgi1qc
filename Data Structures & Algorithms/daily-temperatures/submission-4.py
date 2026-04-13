class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            print(stack, res)
            if not stack:
                stack.append((temp, i))
                continue
            
            # Compare the top value with the current value and see if it is warmer
            # Need to keep looping if a value is popped
            while stack and stack[-1][0] < temp:
                val, index = stack.pop()
                res[index] = i - index
            stack.append((temp, i))
        
        return res

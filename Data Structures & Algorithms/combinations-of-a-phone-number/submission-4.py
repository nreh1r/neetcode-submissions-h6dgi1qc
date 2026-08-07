class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.char_map = {
			"2": ["a", "b", "c"],
			"3": ["d", "e", "f"],
			"4": ["g", "h", "i"],
			"5": ["j", "k", "l"],
			"6": ["m", "n", "o"],
			"7": ["p", "q", "r", "s"],
			"8": ["t", "u", "v"],
			"9": ["w", "x", "y", "z"]
		}
        
        self.res = []

        if not digits:
            return self.res

        def dfs(i, subset):
            if i >= len(digits):
                self.res.append("".join(subset))
                return
            
            for ch in self.char_map[digits[i]]:
                subset.append(ch)
                dfs(i + 1, subset)
                subset.pop()
        
        dfs(0, [])

        return self.res
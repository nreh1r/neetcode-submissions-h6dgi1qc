class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        def dfs(i, subset):
            if i >= len(s):
                self.res.append(subset.copy())
                return
            
            for j in range(i, len(s)):
                substring = s[i:j + 1]
                if substring == substring[::-1]:
                    subset.append(substring)
                    dfs(j + 1, subset)
                    subset.pop()
            
        dfs(0, [])

        return self.res
        
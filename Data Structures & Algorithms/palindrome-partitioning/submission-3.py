class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        def dfs(i, partition):
            if i >= len(s):
                self.res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                substring = s[i:j + 1]
                if substring == substring[::-1]:
                    partition.append(substring)
                    dfs(j + 1, partition)
                    partition.pop()
        
        dfs(0, [])

        return self.res
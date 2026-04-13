class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        
        for i in range(len(s)):
            frequencies, most_frequent = defaultdict(int), 0
            for j in range(i, len(s)):
                frequencies[s[j]] = 1 + frequencies[s[j]]
                most_frequent = max(most_frequent, frequencies[s[j]])
                if (j - i + 1) - most_frequent <= k:
                    longest = max(longest, j - i + 1)

        return longest
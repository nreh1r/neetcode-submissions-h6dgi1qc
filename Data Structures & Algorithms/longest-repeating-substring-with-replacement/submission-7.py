class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        frequencies, most_frequent = defaultdict(int), 0

        l = 0
        for r in range(len(s)):
            frequencies[s[r]] += 1
            most_frequent = max(most_frequent, frequencies[s[r]])

            while (r - l + 1) - most_frequent > k:
                frequencies[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest

        
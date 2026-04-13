class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        frequencies, most_frequent = defaultdict(int), 0

        # Loop from left to right starting a window
        l, r = 0, 0
        while r < len(s):
            frequencies[s[r]] += 1
            most_frequent = max(most_frequent, frequencies[s[r]])

            while (r - l + 1) - most_frequent > k:
                # This means we have hit a substring that has too many characters that aren't the same
                # So remove characters from the left so we can keep going
                frequencies[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        return longest

        
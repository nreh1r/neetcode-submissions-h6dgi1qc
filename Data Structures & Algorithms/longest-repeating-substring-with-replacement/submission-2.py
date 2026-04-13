class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counts, most_frequent = defaultdict(int), 0
        l, r = 0, 0
        
        while r < len(s):
            counts[s[r]] += 1
            most_frequent = max(most_frequent, counts[s[r]])
            
            # Move the left pointer if invalid sequence
            while (r - l + 1) - most_frequent > k:
                counts[s[l]] -= 1
                most_frequent = max(most_frequent, counts[s[l]])
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        return longest
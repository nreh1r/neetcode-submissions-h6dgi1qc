class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0

        for l, a in enumerate(heights):
            r = len(heights) - 1

            while l < r:
                height = min(a, heights[r])
                area = height * (r - l)

                max_val = max(max_val, area)
                r -= 1
        return max_val
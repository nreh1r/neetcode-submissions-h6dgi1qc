class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        while l < len(heights):
            min_height = heights[l]
            curr_max_area = heights[l]
            for r in range(l + 1, len(heights)):
                min_height = min(min_height, heights[r])
                curr_max_area = max(curr_max_area, min_height * (r - l + 1))
            max_area = max(max_area, curr_max_area)
            l += 1
        return max_area
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amount = 0

        while l < r:
            # Calculate the new value for the current position
            distance = r - l
            height = min(heights[l], heights[r])
            curr_amount = distance * height
            max_amount = max(max_amount, curr_amount)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1
        
        return max_amount
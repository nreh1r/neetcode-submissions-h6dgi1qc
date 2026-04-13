class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Map first k numbers
        max_val = nums[0]
        for i in range(1, k):
            max_val = max(max_val, nums[i])
        
        max_nums = [max_val]

        # Loop through the rest of the array
        l = 1
        for r in range(k, len(nums)):
            # Wait till we hit a new window
            new_window = nums[l:r + 1]
            print(new_window)
            new_window.sort()
            max_nums.append(new_window[-1])
            l += 1
        
        return max_nums

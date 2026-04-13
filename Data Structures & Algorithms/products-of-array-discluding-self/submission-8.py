class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # Forward pass to calculate prefixes
        prefix = 1
        for i in range(len(nums)):
            if i == 0:
                res[i] = prefix
                continue
            prefix *= nums[i - 1]
            print(prefix)
            res[i] = prefix
        print(res)

        # Backward pass to calculate postfixes
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                res[i] *= postfix
                continue
            postfix *= nums[i + 1]
            res[i] *= postfix
        
        return res
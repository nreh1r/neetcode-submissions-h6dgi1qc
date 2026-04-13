class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            product = 1
            for j, num in enumerate(nums):
                if i == j:
                    continue
                
                product *= num
            
            output.append(product)
        return output
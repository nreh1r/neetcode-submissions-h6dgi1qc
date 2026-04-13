class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            while numbers[i] + numbers[j] >= target and i < j:
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                j -= 1
            
            i += 1
            j = len(numbers) - 1
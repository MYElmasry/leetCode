class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dif ={}
        for i in range(1, len(numbers)+1):
            if numbers[i-1] in dif :
                return [dif[numbers[i-1]], i]
            else:
                dif[target - numbers[i-1]] = i
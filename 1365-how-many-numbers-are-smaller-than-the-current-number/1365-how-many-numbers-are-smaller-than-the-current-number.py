class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result =[]
        for i in range(len(nums)):
            s = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    s += 1
            result.append(s)
        return result
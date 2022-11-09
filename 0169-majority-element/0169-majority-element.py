class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        for r in range(len(nums)):
            if nums[l] == nums[r]:
                r+=1
                if r - l > len(nums)/2:
                    return nums[l]
            else:
                l = r
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        while r < len(nums):
            if nums[r] == nums[l]:
                nums.pop(r)
            else:
                l = r
                r +=1
        return len(nums)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = list(set(nums))
        if sorted(nums) == sorted(distinct):
            return False
        else:
            return True
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numSet = set(nums)
        counter =  0
        n = len(nums)
        for i in numSet:
            while i in nums:
                nums.pop(nums.index(i))
                counter += 1
            if counter > n/2:
                return i
            counter = 0
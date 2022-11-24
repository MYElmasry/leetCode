class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                result.append(nums2[i])
                nums1.pop(nums1.index(nums2[i]))
        return result
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            midpoint = (left + right) // 2
            if nums[midpoint] == target:
                return midpoint
            elif target > nums[midpoint]:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return -1
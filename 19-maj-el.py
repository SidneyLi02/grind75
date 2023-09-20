class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Implemented Boyer–Moore majority vote algorithm
        # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
        curr, count = nums[0], 0
        for num in nums:
            if num == curr:
                count += 1
            elif count == 0:
                curr, count = num, 1
            else:
                count -= 1
        return curr
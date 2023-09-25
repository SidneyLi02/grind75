class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's algorithm
        best_sum = float('-inf') # largest sum in A[1, ..., k]
        current_sum = 0 # largest sum in A[1, ..., k] ending at k
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum
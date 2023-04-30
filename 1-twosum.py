class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Naive O(n^2)
        # ret = []
        # max = len(nums)
        # for i in range(max):
        #     first = nums[i]
        #     for j in range(i + 1, max):
        #         second = nums[j]
        #         if first + second == target:
        #             ret = [i, j]
        #             break
        # return ret
        
        # Optimal O(n)
        ret = []
        complements = {} # value : index
        max = len(nums)
        for i in range(max):
            complement = target - nums[i]
            complements[complement] = i

        for i in range(max):
            if nums[i] in complements and complements.get(nums[i]) != i:
                ret = [i, complements.get(nums[i])]
                break
        
        return ret

"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""
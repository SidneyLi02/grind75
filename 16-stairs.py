class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # TLE naive method
        # if n == 0 or n == 1:
        #     return 1
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # Tabulation
        # if n == 0 or n == 1:
        #     return 1
        # dp = [0] * (n + 1)
        # dp[0] = dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]
    
        # Space optimization
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n + 1):
            temp = curr
            curr = temp + prev
            prev = temp
        return curr
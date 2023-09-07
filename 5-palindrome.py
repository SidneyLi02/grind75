class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # optimal 2 pointers from sides
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].isalnum() == False:
                left += 1
            elif s[right].isalnum() == False:
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
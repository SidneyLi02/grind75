class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = set()
        for letter in s:
            if letter in t:
                t.remove(letter)
            else:
                t.add(letter)
        if len(t) != 0: # if odd number of a certain letter exists
            return len(s) - len(t) + 1
        else:
            return len(s)
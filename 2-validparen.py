class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        opening = ["(", "[", "{"]
        parenDict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) == 0: return False
                el = stack.pop()
                if parenDict.get(el) != char: return False
                
        if len(stack) != 0: return False
        
        return True
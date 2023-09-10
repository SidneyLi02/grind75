class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # without using Counter class from collections
        missing_dict = {}
        for i in ransomNote:
            if i not in missing_dict:
                missing_dict[i] = 1
            else:
                missing_dict[i] += 1

        for j in magazine:
            if j not in missing_dict:
                missing_dict[j] = -1
            else:
                missing_dict[j] -= 1

        for missing_count in missing_dict.values():
            if missing_count > 0:
                return False
        return True

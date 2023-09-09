class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # two pass hashmap
        count_dict = {}
        for i in s:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] += 1
        
        for j in t:
            if j not in count_dict:
                count_dict[j] = 1
            else:
                count_dict[j] -= 1

        for count in count_dict.values():
            if count != 0:
                return False
        return True
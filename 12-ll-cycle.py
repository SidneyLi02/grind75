# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first, second = head, head
        while first is not None and second is not None:
            first = first.next
            if first is not None:
                first = first.next
            else:
                return False
            second = second.next
            if first == second:
                return True
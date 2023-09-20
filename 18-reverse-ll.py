# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Recursively
        # Consider LinkedList n_1, n_2, ldots, n_k, n_{k + 1}, ldots, n_m
        # Suppose at some point in the algorithm that n_{k + 1}, ldots, n_m are reversed
        # Then we wish for n_{k + 1} next to point to n_k
        # Hence, n_k.next.next = n_{k + 1}.next = n_k
        # if (head is None or head.next is None):
        #     return head
        # else:
        #     p = self.reverseList(head.next)
        #     head.next.next = head
        #     head.next = None
        #     return p

        # Iteratively
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


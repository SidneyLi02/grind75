# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # personal attempt with two pointers (head and tail), iterative O(n)
        ret = ListNode()
        tail = ret

        while list1 is not None or list2 is not None:
            if list1 is None and list2 is not None:
                right = ListNode(list2.val, None)

                tail.next = right
                tail = tail.next

                list2 = list2.next
            elif list1 is not None and list2 is None:
                left = ListNode(list1.val, None)

                tail.next = left
                tail = tail.next

                list1 = list1.next
            else:
                # if neither pointer is None
                left_val = list1.val
                right_val = list2.val

                if left_val < right_val:
                    left = ListNode(list1.val, None)

                    tail.next = left
                    tail = tail.next

                    list1 = list1.next
                else:
                    right = ListNode(list2.val, None)

                    tail.next = right
                    tail = tail.next

                    list2 = list2.next
                
        return ret.next
    
        # personal attempt with recursive approach
        # sol = Solution()
        # if list1 is None and list2 is None:
        #     return None
        # else:
        #     if list1 is None:
        #         return ListNode(list2.val, sol.mergeTwoLists(list1, list2.next))
        #     elif list2 is None:
        #         return ListNode(list1.val, sol.mergeTwoLists(list1.next, list2))
        #     else:
        #         if list1.val < list2.val:
        #             return ListNode(list1.val, sol.mergeTwoLists(list1.next, list2))
        #         else:
        #             return ListNode(list2.val, sol.mergeTwoLists(list1, list2.next))
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Find middle
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Separate second half
        second = slow.next
        slow.next = None

        # Reverse second half
        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Merge
        first = head
        second = prev

        while second:
            a = first.next
            b = second.next

            first.next = second
            second.next = a

            first = a
            second = b
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
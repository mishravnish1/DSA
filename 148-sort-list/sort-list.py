# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        # Base case
        if head is None or head.next is None:
            return head

        # 1. Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split into two lists
        left = head
        right = slow.next
        slow.next = None

        # 3. Sort both halves
        left = self.sortList(left)
        right = self.sortList(right)

        # 4. Merge sorted lists
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        # Attach remaining nodes
        tail.next = left or right

        return dummy.next
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
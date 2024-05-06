# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
        if not head:
            return None
        nextHead = self.removeNodes(head.next)
        if nextHead and nextHead.val > head.val:
            return nextHead
        else:
            head.next = nextHead
            return head

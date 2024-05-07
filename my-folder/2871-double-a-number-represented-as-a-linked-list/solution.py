# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(head):
            if not head:
                return 0, None
            carryOver, nextHead = helper(head.next)
            num = carryOver + head.val * 2
            head.val = num % 10
            return num // 10, head
        
        carryOver, nextHead = helper(head)
        if carryOver:
            return ListNode(1, nextHead)
        else:
            return nextHead

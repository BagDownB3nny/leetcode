# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     # Reverse the linked list that comes after
    #     # Attach that your current node to the back of that list
    #     if head == None or head.next == None:
    #         return head
    #     else:
    #         last_node = head.next
    #         reversed_list = self.reverseList(head.next)
    #         head.next = None
    #         last_node.next = head
    #         return reversed_list

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        next_head = None
        while head != None:
            current_next = head.next
            head.next = next_head
            next_head = head
            head = current_next
        return next_head
        


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        new_list = ListNode()
        start = new_list
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                new_list.next = list1
                new_list = new_list.next
                list1 = list1.next
            else:
                new_list.next = list2
                new_list = new_list.next
                list2 = list2.next
        if list1 != None:
            new_list.next = list1
        elif list2 != None:
            new_list.next = list2
        return start.next

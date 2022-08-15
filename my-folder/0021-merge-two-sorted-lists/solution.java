/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode newList = new ListNode();
        ListNode head = newList;
        while (list1 != null && list2 != null) {
            if (list1.val > list2.val) {
                head.next = list2;
                head = head.next;
                list2 = list2.next;
            } else {
                head.next = list1;
                head = head.next;
                list1 = list1.next;
            }
        }
        if (list1 == null && list2 == null) {
            return newList.next;
        } else  if (list1 == null) {
            head.next = list2;
            return newList.next;
        } else {
            head.next = list1;
            return newList.next;
        }
        
    }
}


/*

2   4
3   5

newList () -> 1124
head           . 
*/

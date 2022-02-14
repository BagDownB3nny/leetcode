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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) {
            return null;
        } else if (l1 == null) {
            l1 = new ListNode(0);
        } else if (l2 == null) {
            l2 = new ListNode(0);
        }
        int v1 = l1.val;
        int v2 = l2.val;
        ListNode newNode = new ListNode(0);
        if (v1 + v2 > 9) {
            newNode.val = v1 + v2 - 10;
            if (l1.next == null) {
                l1.next = new ListNode(0);
            }
            ListNode l3 = l1.next;
            l3.val += 1;
        } else {
            newNode.val = v1 + v2;
            }
        newNode.next = addTwoNumbers(l1.next, l2.next);
        return newNode;
    }
}

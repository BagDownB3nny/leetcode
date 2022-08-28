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
    public ListNode middleNode(ListNode head) {
        int counter = 0;
        ListNode middle = head;
        while (head != null && head.next != null) {
            head = head.next;
            counter += 1;
            if (counter % 2 == 1) {
                middle = middle.next;
            }
        }
        return middle;
    }
}

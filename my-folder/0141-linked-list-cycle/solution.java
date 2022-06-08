/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
import java.util.HashSet;

public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode currentNode = head;
        HashSet set = new HashSet();
        while (currentNode != null && currentNode.next != null) {
            if (set.contains(currentNode)) {
                return true;
            } else {
                set.add(currentNode);
                currentNode = currentNode.next;
            }
        }
        return false;   
    }
}

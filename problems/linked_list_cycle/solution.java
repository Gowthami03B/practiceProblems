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
public class Solution {
    public boolean hasCycle(ListNode head) {
        // To detect if a list is cyclic, we can check whether a node had been visited before. A natural way is to use a hash table.
        // Set<ListNode> map = new HashSet<>();
        // while(head != null){
        //     if(map.contains(head)){
        //         return true;
        //     }
        //     map.add(head);
        //     head = head.next;
        // }
        // return false;
        
        // The space complexity can be reduced to O(1)O(1) by considering two pointers at different speed - a slow pointer and a fast pointer. The slow pointer moves one step at a time while the fast pointer moves two steps at a time.

// If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case. else slow and fast will meet (slow runner completes 1 lap whereas fast runner will do 2 laps but they will meet.) When they meet, there is a cycle.
        if(head == null){
            return false;
        }
        ListNode slow = head;
        ListNode fast = head.next;
        while(slow != fast){
            if(fast == null || fast.next == null){
                return false;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return true;
    }
}
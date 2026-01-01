"""
Question URLs:
LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Question Description:
Given the head of a linked list, remove the N-th node from the end of the list and return its head.

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    vals = []
    cur = head
    while cur:
        vals.append(str(cur.val))
        cur = cur.next
    print("->".join(vals) if vals else "List is empty")


def removeNthFromEnd_bruteforce(head, n):
    """
    Brute Force Approach
    Time Complexity: O(L) where L is the length of the list (two traversals)
    Space Complexity: O(1)

    Steps:
    1. Traverse the list to count nodes (length L).
    2. Calculate the index of node to remove: L - n.
    3. Traverse again to one node before the target and unlink the target node.
    4. Edge case: if to remove first node, return head.next.
    5. Return new head of list.
    """
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    idx_remove = length - n

    dummy = ListNode(0, head)
    cur = dummy
    for _ in range(idx_remove):
        cur = cur.next
    cur.next = cur.next.next if cur.next else None
    return dummy.next


def removeNthFromEnd_optimized(head, n):
    """
    Optimized Approach (Two Pointer/Fast-Slow)
    Time Complexity: O(L) where L is the length of the list (single traversal)
    Space Complexity: O(1)

    Steps:
    1. Use a dummy node before head for edge cases.    
     - Uniform removal logic: You don't need special cases for when the head is deleted; 
       the code for removing any node is the same.
     - Less error-prone: Avoids mistakes like dereferencing None or null pointers.
     - Return value: After manipulation, you can always return dummy.next, 
       which handles any changes to the head pointer, whether or not head was affected.
    2. Move fast pointer n+1 steps ahead.
     - What happens if you only move fast n steps?
        If fast moves n steps ahead, when fast hits the end,
        slow will be on the node to be removed itself, not its previous node.
        This makes it difficult to safely update pointers since you need the previous node 
        to adjust its .next reference.
    3. Move both fast and slow pointers by 1 step until fast reaches end.
    4. Slow will be at node just before the target (n-th from end).
    5. Unlink the target node and return dummy.next.
    """
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    for _ in range(n+1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next if slow.next else None
    return dummy.next


if __name__ == "__main__":
    # Test 1: Remove 2nd node from end in 1->2->3->4->5 (removes 4)
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    print("Original List:")
    print_list(head)

    res_brute = removeNthFromEnd_bruteforce(head, n)
    print("\nAfter Removal (Brute Force):")
    print_list(res_brute)

    # Re-initialize for optimized approach
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res_opt = removeNthFromEnd_optimized(head, n)
    print("\nAfter Removal (Optimized):")
    print_list(res_opt)

    # Test 2: Remove last node (n=1) in single-node list
    head = ListNode(1)
    n = 1
    print("\nSingle-node List Before Removal:")
    print_list(head)
    res_brute_single = removeNthFromEnd_bruteforce(head, n)
    print("After Removal (Brute Force, single node):")
    print_list(res_brute_single)

    head = ListNode(1)
    res_opt_single = removeNthFromEnd_optimized(head, n)
    print("After Removal (Optimized, single node):")
    print_list(res_opt_single)

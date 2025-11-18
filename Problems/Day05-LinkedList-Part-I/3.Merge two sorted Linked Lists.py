"""
Question URLs:
TakeUForward: https://takeuforward.org/data-structure/merge-two-sorted-linked-lists/
LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/

Question Description:
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: l1 = 1->2->4, l2 = 1->3->4
Output: 1->1->2->3->4->4
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    vals = []
    current = head
    while current:
        vals.append(str(current.val))
        current = current.next
    print("->".join(vals))


def mergeTwoLists_bruteforce(l1, l2):
    """
    Brute Force Approach
    Time Complexity: O((n+m) log(n+m)) due to sorting after merging nodes into array
    Space Complexity: O(n+m) for storing nodes in an array

    Steps:
    1. Traverse both linked lists and store values in a list.
    2. Sort the combined list.
    3. Create a new linked list from the sorted list.
    4. Return the head of the new linked list.
    """
    values = []
    current = l1
    while current:
        values.append(current.val)
        current = current.next

    current = l2
    while current:
        values.append(current.val)
        current = current.next

    values.sort()

    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next

    return dummy.next


def mergeTwoLists_optimized(l1, l2):
    """
    Optimized Approach (Two Pointer)
    Time Complexity: O(n + m), where n and m are lengths of the linked lists
    Space Complexity: O(1), uses existing nodes, no extra space

    Steps:
    1. Initialize a dummy node and a pointer tail.
    2. Compare nodes of l1 and l2, attach the smaller one to tail.
    3. Move the pointer of the attached node and tail pointer forward.
    4. After one list ends, attach the remaining nodes of the other list.
    5. Return the next of dummy node (head of merged list).
    """
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2

    return dummy.next


if __name__ == "__main__":
    # Initialize sample linked lists
    # l1: 1->2->4
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    # l2: 1->3->4
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    print("Input List 1:")
    print_list(l1)

    print("Input List 2:")
    print_list(l2)

    print("\nBrute Force Merged List:")
    merged_brute = mergeTwoLists_bruteforce(l1, l2)
    print_list(merged_brute)

    # Need to re-initialize lists as they were modified by previous function
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    print("\nOptimized Merged List:")
    merged_optimized = mergeTwoLists_optimized(l1, l2)
    print_list(merged_optimized)

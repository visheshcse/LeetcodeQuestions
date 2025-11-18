"""
Question URLs:
TakeUForward: https://takeuforward.org/data-structure/reverse-a-linked-list/
LeetCode: https://leetcode.com/problems/reverse-linked-list/

Question Description:
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
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


def reverseList_iterative(head):
    """
    Iterative Approach
    Time Complexity: O(n) where n is length of linked list
    Space Complexity: O(1) constant extra space

    Steps:
    1. Initialize three pointers: prev as None, curr as head.
    2. Iterate the list, set next_node to curr.next.
    3. Point curr.next to prev to reverse the link.
    4. Move prev to curr and curr to next_node.
    5. When curr is None, prev is the new head of reversed list.
    6. Return prev.
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverseList_recursive(head):
    """
    Recursive Approach
    Time Complexity: O(n) where n is length of linked list
    Space Complexity: O(n) due to recursion stack

    Steps:
    1. Base case: if head is None or head.next is None, return head.
    2. Recursively call reverseList_recursive for head.next.
    3. Set head.next.next to head, reversing the link.
    4. Set head.next to None to avoid cycle.
    5. Return new head from the recursion.
    """
    if head is None or head.next is None:
        return head
    new_head = reverseList_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    # Initialize sample linked list: 1->2->3->4->5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("Original List:")
    print_list(head)

    print("\nReversed List (Iterative):")
    reversed_iter = reverseList_iterative(head)
    print_list(reversed_iter)

    # Re-initialize as original list to test recursive method
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("\nReversed List (Recursive):")
    reversed_rec = reverseList_recursive(head)
    print_list(reversed_rec)

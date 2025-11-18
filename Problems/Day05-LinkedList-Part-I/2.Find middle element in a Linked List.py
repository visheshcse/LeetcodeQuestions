"""
Question URLs:
TakeUForward: https://takeuforward.org/data-structure/find-the-middle-element-of-a-linked-list/
LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/

Question Description:
Given a non-empty, singly linked list with head node head, return a middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example:
Input: 1->2->3->4->5
Output: 3

If Input: 1->2->3->4->5->6
Output: 4 (second middle node)
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


def findMiddle_bruteforce_constant_space(head):
    """
    Brute Force Approach with O(1) space
    Time Complexity: O(n) - two traversals
    Space Complexity: O(1)

    Steps:
    1. Traverse list to get count of nodes.
    2. Calculate middle index = count // 2.
    3. Traverse again to the middle index node.
    4. Return the middle node (second middle for even length).
    """
    count = 0
    current = head
    while current:
        count += 1
        current = current.next

    mid_index = count // 2
    current = head
    for _ in range(mid_index):
        current = current.next

    return current


def findMiddle_optimized(head):
    """
    Optimized Approach (Two Pointer Slow and Fast)
    Time Complexity: O(n) - one traversal
    Space Complexity: O(1)

    Steps:
    1. Initialize slow and fast pointers to head.
    2. Move slow pointer by one step, fast pointer by two steps in each iteration.
    3. When fast reaches end (None) or fast.next is None, slow is at middle.
    4. Return slow node (second middle for even length).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    # Initialize sample linked list: 1->2->3->4->5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("Input List:")
    print_list(head)

    middle_node_brute = findMiddle_bruteforce_constant_space(head)
    print(f"Middle Node (Brute Force O(1) space): {middle_node_brute.val}")

    middle_node_optimized = findMiddle_optimized(head)
    print(f"Middle Node (Optimized): {middle_node_optimized.val}")

    # Test with even number of nodes: 1->2->3->4->5->6
    head_even = ListNode(1, 
                        ListNode(2, 
                                 ListNode(3, 
                                          ListNode(4, 
                                                   ListNode(5, 
                                                            ListNode(6))))))
    print("\nInput Even List:")
    print_list(head_even)

    middle_node_brute_even = findMiddle_bruteforce_constant_space(head_even)
    print(f"Middle Node (Brute Force O(1) space, even list): {middle_node_brute_even.val}")

    middle_node_optimized_even = findMiddle_optimized(head_even)
    print(f"Middle Node (Optimized, even list): {middle_node_optimized_even.val}")

"""
Question URL:
LeetCode: https://leetcode.com/problems/delete-node-in-a-linked-list/

Question Description:
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, only the node to be deleted.
It is guaranteed that the node to be deleted is not the tail node.

Example:
Input: Linked List = [4,5,1,9], Node = 5
Output: [4,1,9]
Explanation: Given node with value 5, after deletion list becomes 4->1->9.
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

def deleteNode_optimized(node):
    """
    Optimized Approach
    Time Complexity: O(1)
    Space Complexity: O(1)

    Steps:
    1. Copy data from the next node into the node to be deleted.
    2. Change the node's next pointer to point to its next node's next.
    3. This effectively removes the node from the list (since direct removal isn't possible without access to the previous node).
    """
    node.val = node.next.val
    node.next = node.next.next

if __name__ == "__main__":
    # Initialize sample linked list: 4->5->1->9
    head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
    print("Original List:")
    print_list(head)

    # Identify node to delete (node with value 5)
    node_to_delete = head.next

    deleteNode_optimized(node_to_delete)
    print("\nList After Deletion (Optimized):")
    print_list(head)

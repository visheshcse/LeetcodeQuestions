"""
LeetCode URL: https://leetcode.com/problems/copy-list-with-random-pointer/

Question Description:
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointers of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
- val: The value of the node.
- random_index: The index of the node pointed to by the random pointer, or null if it does not point to any node.

Constraints:
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is null or points to a node in the linked list.
"""

#########################################################
# Brute Force Approach: Using HashMap
#########################################################

class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random
    def __repr__(self):
        return f"Node(val={self.val})"

def copyRandomList_brute(head):
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    Algorithm Steps:
    1. Traverse the original linked list and create a hash map (dictionary) that maps each original node to its newly created copy.
    2. Traverse the list again, for each original node, assign the copied node's `next` pointer as the copy of the original node's `next`, and similarly for the `random` pointer, using the hash map.
    3. Return the head of the copied list from the hash map.
    """
    if head is None:
        return None

    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head]


#########################################################
# Optimized Approach: Interleaving Nodes
#########################################################

def copyRandomList_optimized(head):
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Algorithm Steps:
    1. For each node in the original list, create a copy node and insert it right after the original node, interleaving the original and copied nodes.
    2. Traverse the interleaved list again, set the `random` pointer of each copied node to the copied node corresponding to the original node's `random` (i.e., original node's `random.next`).
    3. Separate the interleaved nodes to restore the original list and extract the copied list by adjusting `next` pointers.
    4. Return the head of the deep-copied list.
    """
    if head is None:
        return None
    
    curr = head
    while curr:
        new_node = Node(curr.val, curr.next)
        curr.next = new_node
        curr = new_node.next
    
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    curr = head
    pseudo_head = Node(0)
    copy_curr = pseudo_head
    while curr:
        copy_curr.next = curr.next
        curr.next = curr.next.next
        curr = curr.next
        copy_curr = copy_curr.next

    return pseudo_head.next


#########################################################
# Helper Function to Print the List for Verification
#########################################################

def printList(head):
    nodes = []
    curr = head
    while curr:
        rand = curr.random.val if curr.random else None
        nodes.append(f"[Val:{curr.val} Rand:{rand}]")
        curr = curr.next
    print("->".join(nodes))


#########################################################
# Sample Initialization and Execution
#########################################################

# Example: 1 -> 2 -> 3, with random pointers
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node1.random = node3
node2.random = node1
node3.random = node2

print("Original list:")
printList(node1)

cloned_brute = copyRandomList_brute(node1)
print("
Cloned list using Brute Force:")
printList(cloned_brute)

cloned_opt = copyRandomList_optimized(node1)
print("
Cloned list using Optimized Approach:")
printList(cloned_opt)
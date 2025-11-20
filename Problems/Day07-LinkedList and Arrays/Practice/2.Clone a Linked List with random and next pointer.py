"""
Question URL:
LeetCode: https://leetcode.com/problems/copy-list-with-random-pointer/

Question Description:
A linked list of length n is given, where each node contains an additional random pointer,
which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

Example:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def print_list(head):
    out = []
    temp=head
    idx_map={}
    idx=0
    while temp:
        idx_map[temp]=idx
        idx +=1
        temp=temp.next
    temp=head
    while temp:
        random_idx=idx_map[temp.random] if temp.random else None
        out.append(str([temp.val, random_idx]))
        temp =temp.next
    print("->".join(out))



def copyRandomList_hashmap(head):

    """
    Hash Map (Iterative) Approach
    Time Complexity: O(n)
    Space Complexity: O(n)

    Steps:
    1. First pass: Create all new nodes and map each original node to its copy using a hash map.
    2. Second pass: Assign next and random pointers using the hash map.
    3. Return the head of the copied list.
    """
    if not head:
        return head
    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val, curr.next)
        curr = curr.next
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr .next
    return old_to_new[head]


def copyRandomList_interleaving(head):
    """
    Interleaving Node Approach
    Time Complexity: O(n)
    Space Complexity: O(1) (excluding output list)

    Steps:
    1. First pass: Interleave copy nodes with original list.
    2. Second pass: Assign random pointers to copied nodes.
    3. Third pass: Separate the copied list from original.
    4. Return copied head.
    """
    if not head:
        return head
    
    curr = head
    while curr:
        nxt = curr.next
        curr.next = Node(curr.val, curr.next)
        curr=nxt

    curr =head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    
    orig=head
    copy_head = orig.next
    copy = copy_head
    while orig:
        orig.next=orig.next.next
        copy.next =copy.next.next if copy.next else None
        orig=orig.next
        copy=copy.next
    return copy_head
    




def copyRandomList_recursive(head):
    """
    Recursive Approach with Memoization (Hash Map)
    Time Complexity: O(n)
    Space Complexity: O(n) for memoization and call stack

    Steps:
    1. Use recursion to clone each node, storing mapping from old node to new.
    2. Base case: If node is None, return None.
    3. If node has already been copied, return it from map.
    4. Recursively assign next and random pointers for every node.
    """
    def clone(head, old_to_new):
        if not head:
            return head
        if head in old_to_new:
            return old_to_new[head]
        copy = Node(head.val, None)
        old_to_new[head] = copy
        copy.next = clone(head.next, old_to_new)
        copy.random = clone(head.random, old_to_new)
        return copy
    return clone(head, {})


if __name__ == "__main__":
    # Sample setup: [7,null],[13,0],[11,4],[10,2],[1,0]
    a = Node(7)
    b = Node(13)
    c = Node(11)
    d = Node(10)
    e = Node(1)
    a.next, b.next, c.next, d.next = b, c, d, e
    a.random, b.random, c.random, d.random, e.random = None, a, e, c, a
    sample_head = a

    print("Original List:")
    print_list(sample_head)

    print("\nHash Map (Iterative) Approach:")
    copied1 = copyRandomList_hashmap(sample_head)
    print_list(copied1)

    print("\nInterleaving (Optimized) Approach:")
    # Re-init sample as previous may alter structure
    a = Node(7)
    b = Node(13)
    c = Node(11)
    d = Node(10)
    e = Node(1)
    a.next, b.next, c.next, d.next = b, c, d, e
    a.random, b.random, c.random, d.random, e.random = None, a, e, c, a
    sample_head2 = a
    copied2 = copyRandomList_interleaving(sample_head2)
    print_list(copied2)

    print("\nRecursive Approach with Memoization:")
    # Re-init sample for a fresh recursive run
    a = Node(7)
    b = Node(13)
    c = Node(11)
    d = Node(10)
    e = Node(1)
    a.next, b.next, c.next, d.next = b, c, d, e
    a.random, b.random, c.random, d.random, e.random = None, a, e, c, a
    sample_head3 = a
    copied3 = copyRandomList_recursive(sample_head3)
    print_list(copied3)

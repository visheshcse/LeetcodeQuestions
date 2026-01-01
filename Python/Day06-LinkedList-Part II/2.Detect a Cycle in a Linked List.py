# LeetCode Problem URL: https://leetcode.com/problems/linked-list-cycle/
#
# Problem Description:
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
#
# Return True if there is a cycle in the linked list. Otherwise, return False.
#
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: True
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#
# Example 2:
# Input: head = [1,2], pos = 0
# Output: True
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
#
# Example 3:
# Input: head = [1], pos = -1
# Output: False
# Explanation: There is no cycle in the linked list.
#
# Constraints:
# - The number of the nodes in the list is in the range [0, 10^4].
# - -10^5 <= Node.val <= 10^5
# - pos is -1 or a valid index in the linked-list.
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#########################################################
# Approach 1: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)
#########################################################
class Solution:
    def hasCycle_hash(self, head: ListNode) -> bool:
        """
        Hash Set approach:
        1. Traverse the list storing each node reference in a set.
        2. If you encounter a node already in the set, a cycle exists.
        3. If you reach the end (None), no cycle exists.
        """
        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False

#########################################################
# Approach 2: Two Pointers (Floyd's Tortoise and Hare)
# Time Complexity: O(n)
# Space Complexity: O(1)
#########################################################
    def hasCycle_two_pointer(self, head: ListNode) -> bool:
        """
        Two Pointers (Floyd's Tortoise and Hare):
        1. Use two pointers, slow advances one step, fast two steps.
        2. If they ever meet, cycle exists.
        3. If fast reaches the end, no cycle.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#########################################################
# Approach 3: Brute Force (Mark visited by changing structure)
# Time Complexity: O(n)
# Space Complexity: O(1) and destructive
#########################################################
    def hasCycle_brute_force(self, head: ListNode) -> bool:
        """
        Brute force: Temporarily modify nodes to indicate visited
        (not recommended in interviews as this destructs structure).
        """
        current = head
        while current:
            if hasattr(current, 'visited'):
                return True
            setattr(current, 'visited', True)
            current = current.next
        return False

#########################################################
# Example Initialization and Demo Run
#########################################################
def build_list_with_cycle():
    """
    Build a list [3,2,0,-4] with a cycle at position 1:
    3 -> 2 -> 0 -> -4 (cycle to 2)
    """
    nodes = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    nodes[-1].next = nodes[1]  # cycle here
    return nodes[0]

def build_list_no_cycle():
    """
    Build a list [1,2,3,4,5] with no cycle.
    """
    nodes = [ListNode(i) for i in [1,2,3,4,5]]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    return nodes[0]

if __name__ == "__main__":
    sol = Solution()

    head_cycle = build_list_with_cycle()
    head_nocycle = build_list_no_cycle()

    print("HashSet approach output [cycle]:", sol.hasCycle_hash(head_cycle))
    print("HashSet approach output [no cycle]:", sol.hasCycle_hash(head_nocycle))
    print("Two pointer approach output [cycle]:", sol.hasCycle_two_pointer(head_cycle))
    print("Two pointer approach output [no cycle]:", sol.hasCycle_two_pointer(head_nocycle))
    print("Brute-force (destructive) approach output [cycle]:", sol.hasCycle_brute_force(head_cycle))
    print("Brute-force (destructive) approach output [no cycle]:", sol.hasCycle_brute_force(head_nocycle))

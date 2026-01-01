# LeetCode Problem URL: https://leetcode.com/problems/linked-list-cycle-ii/
#
# Problem Description:
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
# Note: pos is not passed as a parameter.
#
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
#
# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
#
# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
#
# Constraints:
# - The number of the nodes in the list is in the range [0, 10^4].
# - -10^5 <= Node.val <= 10^5
# - pos is -1 or a valid index in the linked-list.
#
# Follow up: Can you solve it using O(1) (constant) memory?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#######################################################
# Approach 1: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)
#######################################################
class Solution:
    def detectCycle_hash(self, head: ListNode) -> ListNode:
        """
        HashSet approach:
        1. Traverse the list storing node references in a set.
        2. Return the first node seen twice (cycle start), else None.
        """
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
            curr = curr.next
        return None

#######################################################
# Approach 2: Floyd’s Cycle Detection (Tortoise and Hare) algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
#######################################################
    def detectCycle_floyd(self, head: ListNode) -> ListNode:
        """
        Floyd’s Cycle Detection (Tortoise and Hare) algorithm:

        - Uses two pointers moving at different speeds through the linked list:
            slow moves 1 step at a time, fast moves 2 steps.
        - If no cycle, fast pointer reaches the end (null).
        - If cycle exists, slow and fast pointers must meet inside the cycle.
        
        Mathematical reasoning:
        Let:
            L = distance from head to start of loop,
            C = length of the loop,
            x = distance from start of loop to meeting point in loop.
        
        At meeting:
            Distance travelled by slow = L + x
            Distance travelled by fast = L + x + n*C (fast has made n full loops)
        
        Since fast moves twice as fast:
            2(L + x) = L + x + n*C
            => L + x = n*C
            => L = n*C - x
        
        This implies that if we move one pointer back to head, and keep the other at meeting point,
        then advancing both one step at a time will make them meet at the loop start after L steps.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        # If you exit the loop via break, the else is skipped.
        # If you exit because the condition became False, the else executes.
        
        # We can use this as well
        # if fast is None or fast.next is None:
        #     return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

#######################################################
# Approach 3: Brute-force (changing structure, not recommended)
# Time Complexity: O(n)
# Space Complexity: O(1), but destructive
#######################################################
    def detectCycle_bruteforce(self, head: ListNode) -> ListNode:
        """
        Brute force (Destructive marking, not recommended):
        Mark nodes with visited flag.
        """
        curr = head
        while curr:
            if hasattr(curr, 'visited'):
                return curr
            curr.visited = True
            curr = curr.next
        return None

#######################################################
# Helper Functions for Testing
#######################################################
def build_list_with_cycle(vals, pos):
    """
    Build a cycle list from vals; the tail connects to node at index pos.
    """
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None

def show_cycle_start(node):
    if node:
        print(f"Cycle starts at node with value: {node.val}")
    else:
        print("No cycle detected.")

#######################################################
# Demo Run
#######################################################
if __name__ == "__main__":
    vals, pos = [3,2,0,-4], 1
    head = build_list_with_cycle(vals, pos)
    sol = Solution()
    print("HashSet approach output:")
    show_cycle_start(sol.detectCycle_hash(head))
    head = build_list_with_cycle(vals, pos)
    print("Floyd's algorithm output:")
    show_cycle_start(sol.detectCycle_floyd(head))
    head = build_list_with_cycle(vals, pos)
    print("Brute-force approach output:")
    show_cycle_start(sol.detectCycle_bruteforce(head))
    # Non-cycle case
    head = build_list_with_cycle([1,2,3,4], -1)
    print("Floyd's output (no cycle):")
    show_cycle_start(sol.detectCycle_floyd(head))

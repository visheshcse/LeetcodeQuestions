# LeetCode Problem URL: https://leetcode.com/problems/reverse-nodes-in-k-group/
#
# Problem Description:
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k, leave the last nodes as they are.
# You may not alter the values in the list’s nodes—only nodes themselves may be changed.
#
# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
#
# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
# Constraints:
# - 1 <= k <= n <= 5000 (n is length of list)
# - 0 <= Node.val <= 1000
# Follow-up: Solve in O(1) extra memory.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

##############################################################
# Approach 1: Iterative Group Reversal
# Time Complexity: O(n)
# Space Complexity: O(1)
##############################################################

class Solution:
    def reverseKGroup_iterative(head: ListNode, k: int) -> ListNode:
        """
        Iterative approach to reverse nodes in k-group:
        1. Use a dummy node for easier handling of head reversals.
        2. For each k-sized group, reverse the group.
        3. Connect the reversed group back to the previous part.
        4. If the nodes left are fewer than k, leave as is.
        Time: O(n)
        Space: O(1)
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        def get_kth_node(start, steps):
            # Return the k-th node from start, or None if not enough nodes
            current = start
            count = 0
            while current and count < steps:
                current = current.next
                count += 1
            return current

        while True:
            kth = get_kth_node(group_prev, k)  # Find the kth node from group_prev
            if not kth:
                break  # Fewer than k nodes left—stop
            next_group_head = kth.next         # Save the next group's first node

            # Reverse the k nodes
            prev, curr = next_group_head, group_prev.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Reconnect the reversed segment with the previous and next section
            old_group_start = group_prev.next
            group_prev.next = kth          # kth is new group head after reversal
            group_prev = old_group_start   # Move group_prev to end of new reversed group

        return dummy.next



##############################################################
# Approach 2: Recursive Group Reversal
# Time Complexity: O(n)
# Space Complexity: O(n/k) (due to recursion stack)
##############################################################

    def reverseKGroup_recursive(self, head: ListNode, k: int) -> ListNode:
        """
        Recursive approach:
        1. Check if enough nodes remain for a full group.
        2. Reverse first k nodes and recursively call for the next group.
        3. Connect reversed part with the result of recursion.
        """
        curr = head
        cnt = 0
        while curr and cnt < k:
            curr = curr.next
            cnt += 1
        if cnt < k:
            return head
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head.next = self.reverseKGroup_recursive(curr, k)
        return prev

##############################################################
# Helper: Convert list to linked list for testing
##############################################################
def build_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

##############################################################
# Demo Run
##############################################################
if __name__ == "__main__":
    head = build_list([1,2,3,4,5])
    k = 2
    sol = Solution()
    print("Iterative approach output:")
    print_list(sol.reverseKGroup_iterative(head, k))
    head = build_list([1,2,3,4,5])  # Rebuild list for recursive (previously mutated)
    print("Recursive approach output:")
    print_list(sol.reverseKGroup_recursive(head, k))

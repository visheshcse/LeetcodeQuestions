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
    def reverseKGroup_iterative(self, head: ListNode, k: int) -> ListNode:
        """
        Iterative approach:
        1. Use a dummy node to ease edge cases.
        2. Count total number of nodes.
        3. For each group of k, reverse nodes in-place.
        4. Connect reversed with previously processed nodes.
        5. If fewer than k remain, leave as-is.
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        def get_kth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            
            # Reverse group
            prev, curr = kth.next, group_prev.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
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

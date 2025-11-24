# LeetCode Problem URL: https://leetcode.com/problems/palindrome-linked-list/
#
# Problem Description:
# Given the head of a singly linked list, return True if it is a palindrome or False otherwise.
#
# Example 1:
# Input: head = [1,2,2,1]
# Output: True
#
# Example 2:
# Input: head = [1,2]
# Output: False
#
# Constraints:
# - The number of nodes in the list is in the range [1, 10^5].
# - 0 <= Node.val <= 9
#
# Follow up: Could you do it in O(n) time and O(1) space?

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#######################################################
# Approach 1: Array/Stack (store all values)
# Time Complexity: O(n)
# Space Complexity: O(n)
#######################################################
class Solution:
    def isPalindrome_array(self, head: ListNode) -> bool:
        """
        Array approach:
        1. Traverse the list, storing all node values in an array.
        2. Use two-pointer technique or compare to reversed array to check for palindrome.
        """
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        return vals == vals[::-1]

#######################################################
# Approach 2: Stack (compare entire list to reverse via stack)
# Time Complexity: O(n)
# Space Complexity: O(n)
#######################################################
def is_palindrome_stack(head: ListNode) -> bool:
    """
    Stack approach: Traverse and compare node values to reversed order via stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    current = head
    while current:
        stack.append(current.val)
        current = current.next
    while head:
        if head.val != stack.pop():
            return False
        head = head.next
    return True

#######################################################
# Approach 3: Stack (compare half, space O(n/2))
# Time Complexity: O(n)
# Space Complexity: O(n)
#######################################################
class Solution(Solution):  # To inherit previous methods
    def isPalindrome_stack_half(self, head: ListNode) -> bool:
        """
        Stack + fast/slow pointer (compare half).
        """
        slow = fast = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        return True

#######################################################
# Approach 4: Reverse Second Half (O(1) Space)
# Time Complexity: O(n)
# Space Complexity: O(1)
#######################################################
    def isPalindrome_reverse(self, head: ListNode) -> bool:
        """
        Two pointer and reverse second half:
        1. Use fast/slow pointers to find middle of the list.
        2. Reverse second half in-place.
        3. Walk from start and from middle, comparing values.
        """
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

#######################################################
# Approach 5: Recursion
# Time Complexity: O(n)
# Space Complexity: O(n) (due to call stack)
#######################################################
    def isPalindrome_recursion(self, head: ListNode) -> bool:
        """
        Recursive approach:
        Use recursion to compare values from ends inward, leveraging call stack.
        """
        self.front_pointer = head
        def recursively_check(current):
            if current is not None:
                if not recursively_check(current.next):
                    return False
                if self.front_pointer.val != current.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        return recursively_check(head)

#######################################################
# Helper Functions for Testing
#######################################################
def build_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_result(val):
    print("Palindrome" if val else "Not palindrome")

#######################################################
# Demo Run
#######################################################
if __name__ == "__main__":
    head = build_list([1,2,2,1])
    sol = Solution()
    print("Array approach output:", sol.isPalindrome_array(head))
    head = build_list([1,2,2,1])
    print("Full stack approach output:", is_palindrome_stack(head))
    head = build_list([1,2,2,1])
    print("Half stack (fast/slow) approach output:", sol.isPalindrome_stack_half(head))
    head = build_list([1,2,2,1])
    print("Reverse and compare approach output:", sol.isPalindrome_reverse(head))
    head = build_list([1,2,2,1])
    print("Recursive approach output:", sol.isPalindrome_recursion(head))
    head = build_list([1,2])
    print("Not-palindrome (full stack) output:", is_palindrome_stack(head))

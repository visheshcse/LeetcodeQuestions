"""
Question URLs:
LeetCode: https://leetcode.com/problems/add-two-numbers/

Question Description:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each node contains a single digit. 
Add the two numbers and return the sum as a linked list.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
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

def addTwoNumbers_bruteforce(l1, l2):
    """
    Brute Force Approach
    Time Complexity: O(max(n, m)) for traversal and addition (n and m are lengths of lists)
    Space Complexity: O(n + m) due to use of additional storage in each step

    Steps:
    1. Traverse both linked lists, extract numbers as strings, reverse and convert to integers.
    2. Add both numbers to get total.
    3. Convert total back to string, reverse, and create new linked list nodes.
    4. Return new list head.
    """
    num1 = []
    num2 = []
    while l1:
        num1.append(str(l1.val))
        l1 = l1.next
    while l2:
        num2.append(str(l2.val))
        l2 = l2.next
    
    n1 = int(''.join(num1[::-1]))
    n2 = int(''.join(num2[::-1]))
    total = str(n1 + n2)[::-1]

    dummy = ListNode()
    curr = dummy
    for digit in total:
        curr.next = ListNode(int(digit))
        curr = curr.next

    return dummy.next

def addTwoNumbers_optimized(l1, l2):
    """
    Optimized Approach (Digit by Digit Addition)
    Time Complexity: O(max(n, m)) for traversing both lists (n and m are lengths)
    Space Complexity: O(max(n, m)) for result linked list

    Steps:
    1. Traverse both lists simultaneoulsy.
    2. At each step, add digits and carry.
    3. Create a new node with result digit, update carry.
    4. Continue until both lists are exhausted and carry is zero.
    5. Return dummy.next as new head.
    """
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

if __name__ == "__main__":
    # Initialize sample lists l1: 2->4->3 (represents 342)
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    # l2: 5->6->4 (represents 465)
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    print("Input List 1:")
    print_list(l1)
    print("Input List 2:")
    print_list(l2)

    print("\nResult (Brute Force):")
    sum_brute = addTwoNumbers_bruteforce(l1, l2)
    print_list(sum_brute)

    # Re-initialize (as lists are consumed in brute force function)
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    print("\nResult (Optimized):")
    sum_opt = addTwoNumbers_optimized(l1, l2)
    print_list(sum_opt)

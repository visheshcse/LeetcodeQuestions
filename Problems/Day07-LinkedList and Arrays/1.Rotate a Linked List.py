# LeetCode problem: https://leetcode.com/problems/rotate-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRightBruteForce(head, k):
    """
    Time Complexity: O(k * n) where n is length of list.
    Space Complexity: O(1)

    Rotate a linked list to the right by k places using brute force.
    This involves moving the last node of the list to the
    front k times. For each rotation, traverse to the end,
    remove last node and attach it at the head.
    """
    if not head or not head.next or k == 0:
        return head

    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    k = k % length
    if k == 0:
        return head

    for _ in range(k):
        prev = None
        current = head
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        current.next = head
        head = current

    return head

def rotateRightOptimized(head, k):
    """
    Time Complexity: O(n) where n is length of list.
    Space Complexity: O(1)

    Rotate a linked list to the right by k places using an optimized approach.
    First, compute the list length and make it circular by connecting the tail to head.
    Then break the circle at the new tail position which is (length - k)th node.
    """
    if not head or not head.next or k == 0:
        return head

    length = 1
    last = head
    while last.next:
        last = last.next
        length += 1

    k = k % length
    if k == 0:
        return head

    last.next = head
    temp = head
    for _ in range(length - k - 1):
        temp = temp.next

    new_head = temp.next
    temp.next = None

    return new_head

def printList(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return '->'.join(values)

# Simple linked list 1->2->3
head = ListNode(1, ListNode(2, ListNode(3)))

# Run brute force rotation by 1
rotated_brute = rotateRightBruteForce(head, 1)
print("List after brute force rotation by 1:", printList(rotated_brute))

# Run optimized rotation by 2
rotated_opt = rotateRightOptimized(rotated_brute, 2)
print("List after optimized rotation by 2:", printList(rotated_opt))

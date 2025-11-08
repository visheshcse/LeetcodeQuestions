class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Sample linked list initialization: 1 -> 2 -> 3 -> 2 -> 1
def create_sample_linked_list():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    return head

# Stack method to check palindrome
def is_palindrome_stack(head: ListNode) -> bool:
    """
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

# Reverse half method to check palindrome
def is_palindrome_reverse(head: ListNode) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return True

    # Find middle using fast and slow pointers
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Compare first and second half
    first, second = head, prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True

# Driver code to demonstrate both methods
if __name__ == "__main__":
    head = create_sample_linked_list()

    print("Using Stack Method:")
    print(is_palindrome_stack(head))  # Expected output: True

    print("Using Reverse Half Method:")
    print(is_palindrome_reverse(head))  # Expected output: True

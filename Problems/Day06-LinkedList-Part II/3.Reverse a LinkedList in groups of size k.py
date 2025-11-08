class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper to create a sample linked list for testing: 1->2->3->4->5->6->7->8->None
def create_sample_linked_list():
    head = ListNode(1)
    current = head
    for i in range(2, 9):
        current.next = ListNode(i)
        current = current.next
    return head

def print_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

def reverse_k_group(head: ListNode, k: int) -> ListNode:
    """
    Reverses the linked list in groups of size k.
    Time Complexity: O(n) - Each node is processed once.
    Space Complexity: O(1) - In-place reversal.

    Steps:
    - Reverse first k nodes.
    - Recursively call for remaining list.
    - Connect reversed part with returned head from recursion.
    """
    current = head
    count = 0

    # Check if there are at least k nodes left in list
    temp = current
    for _ in range(k):
        if not temp:
            return head  # Less than k nodes, no reversal
        temp = temp.next

    # Reverse k nodes
    prev = None
    while current and count < k:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        count += 1

    # head now is the last node in reversed group, connect to next reversed group
    if current:
        head.next = reverse_k_group(current, k)

    return prev  # New head of reversed group

if __name__ == "__main__":
    head = create_sample_linked_list()
    print("Original List:")
    print_list(head)

    k = 3
    reversed_head = reverse_k_group(head, k)
    print(f"List after reversing in groups of {k}:")
    print_list(reversed_head)

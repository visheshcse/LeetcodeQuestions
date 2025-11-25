# Problem Statement: Given a linked list containing ‘N’ head nodes where every node in the linked list contains two pointers:

# ‘Next’ points to the next node in the list
# ‘Child’ pointer to a linked list where the current node is the head
# Each of these child linked lists is in sorted order and connected by a 'child' pointer. 
# Your task is to flatten this linked list such that all nodes appear in a single layer or level in a 'sorted order'.


class Node:
    def __init__(self, data=0, next=None, bottom=None):
        self.data = data
        self.next = next      # Pointer to next list in the horizontal direction
        self.bottom = bottom  # Pointer to next node in the vertical direction (linked list to flatten)

# Helper function to create sample linked list of linked lists
def create_sample_linked_list():
    # Example structure:
    # 5 -> 10 -> 19 -> 28
    # |     |     |     |
    # 7     20    22    35
    # |           |     |
    # 8           50    40
    # |                 |
    # 30                45

    head = Node(5)
    head.bottom = Node(7)
    head.bottom.bottom = Node(8)
    head.bottom.bottom.bottom = Node(30)

    head.next = Node(10)
    head.next.bottom = Node(20)

    head.next.next = Node(19)
    head.next.next.bottom = Node(22)
    head.next.next.bottom.bottom = Node(50)

    head.next.next.next = Node(28)
    head.next.next.next.bottom = Node(35)
    head.next.next.next.bottom.bottom = Node(40)
    head.next.next.next.bottom.bottom.bottom = Node(45)

    return head

# Method 1: Flatten by converting all nodes to array, sort, and reconstruct list
def flatten_using_array(head: Node) -> Node:
    """
    Time Complexity: O(N log N) where N is total nodes (flattened)
    Space Complexity: O(N) for the array holding all nodes
    
    Steps:
    - Traverse all nodes using next and bottom pointers, collect values in array.
    - Sort the array.
    - Create a new flattened linked list using bottom pointers.
    """
    if not head:
        return None

    values = []
    current = head
    # Traverse horizontally and vertically to collect all values
    while current:
        temp = current
        while temp:
            values.append(temp.data)
            temp = temp.bottom
        current = current.next

    values.sort()

    # Rebuild flattened linked list using bottom pointers
    dummy = Node(0)
    curr = dummy
    for val in values:
        curr.bottom = Node(val)
        curr = curr.bottom

    return dummy.bottom

# Method 2: Flatten by merging sorted linked lists (merge two sorted lists)
def merge_lists(a: Node, b: Node) -> Node:
    """Merge two sorted bottom linked lists."""
    if not a:
        return b
    if not b:
        return a
    if a.data <= b.data:
        result =a
        result.bottom = merge_lists(a.bottom, b)
    else:
        result=b
        result.bottom = merge_lists(a, b.bottom)
    result.next=None
    return result
    

def flatten_by_merge(head: Node) -> Node:
    """
    Time Complexity: O(N * M) - merging all vertical lists N times, each with M avg length
    Space Complexity: O(1) - merges done in place
    
    Steps:
    - Recursively flatten the next lists.
    - Merge current list with the flattened next list.
    """
    if not head or not head.next:
        return head
    head.next = flatten_by_merge(head.next)
    head = merge_lists(head, head.next)
    return head
    

# Utility to print the flattened list using bottom pointers
def print_flattened_list(head: Node):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.bottom
    print()

if __name__ == "__main__":
    head = create_sample_linked_list()

    print("Flattening linked list using array method:")
    flattened_array = flatten_using_array(head)
    print_flattened_list(flattened_array)

    # Re-create list as previous was not modified
    head = create_sample_linked_list()
    print("Flattening linked list using merge sorted lists method:")
    flattened_merge = flatten_by_merge(head)
    print_flattened_list(flattened_merge)

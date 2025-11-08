class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper to create intersecting linked lists for testing
def create_intersecting_lists():
    # List A: 1 -> 2 -> 3
    #                      \
    #                       6 -> 7
    #                      /
    # List B:       4 -> 5
    #
    # Intersection starts at node with value 6

    intersect = ListNode(6, ListNode(7))

    headA = ListNode(1, ListNode(2, ListNode(3, intersect)))
    headB = ListNode(4, ListNode(5, intersect))

    return headA, headB, intersect

def print_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Method 1: Brute Force
def get_intersection_node_bruteforce(headA: ListNode, headB: ListNode) -> ListNode:
    """
    Time Complexity: O(m*n)
    Space Complexity: O(1)
    
    For each node in list A, check all nodes in list B for match.
    """
    currentA = headA
    while currentA:
        currentB = headB
        while currentB:
            if currentA == currentB:
                return currentA
            currentB = currentB.next
        currentA = currentA.next
    return None

# Method 2: Hashing
def get_intersection_node_hash(headA: ListNode, headB: ListNode) -> ListNode:
    """
    Time Complexity: O(m + n)
    Space Complexity: O(m)
    
    Store all nodes of list A in a set for quick lookup.
    Then traverse list B checking if nodes are in the set.
    """
    nodes_set = set()
    current = headA
    while current:
        nodes_set.add(current)
        current = current.next

    current = headB
    while current:
        if current in nodes_set:
            return current
        current = current.next

    return None

# Method 3: Difference in Length
def get_intersection_node_diff_length(headA: ListNode, headB: ListNode) -> ListNode:
    """
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    
    Steps:
    - Calculate lengths of both lists.
    - Advance longer list by the difference in lengths.
    - Move both pointers until they meet or reach end.
    """
    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    lenA = get_length(headA)
    lenB = get_length(headB)

    currentA = headA
    currentB = headB

    if lenA > lenB:
        for _ in range(lenA - lenB):
            currentA = currentA.next
    else:
        for _ in range(lenB - lenA):
            currentB = currentB.next

    while currentA and currentB:
        if currentA == currentB:
            return currentA
        currentA = currentA.next
        currentB = currentB.next

    return None

if __name__ == "__main__":
    headA, headB, intersect = create_intersecting_lists()
    print("List A:")
    print_list(headA)
    print("List B:")
    print_list(headB)
    
    node = get_intersection_node_bruteforce(headA, headB)
    print("Brute Force Intersection at node with value:", node.val if node else None)
    
    node = get_intersection_node_hash(headA, headB)
    print("Hashing Intersection at node with value:", node.val if node else None)
    
    node = get_intersection_node_diff_length(headA, headB)
    print("Difference in Length Intersection at node with value:", node.val if node else None)

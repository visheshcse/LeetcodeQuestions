class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a sample linked list with a loop for demonstration
# Example list: 1 -> 2 -> 3 -> 4 -> 5
#                         ^         |
#                         |_________|
def create_sample_linked_list_with_loop():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # Creating a loop here (node 5 points back to node 3)
    head.next.next.next.next.next = head.next.next
    return head

def find_loop_start_floyd(head: ListNode) -> ListNode:
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
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

def find_loop_start_visited(head: ListNode) -> ListNode:
    """
    Tracks visited nodes in a set to find the start of the loop.
    Time Complexity: O(n) - visits each node once.
    Space Complexity: O(n) - extra space for storing visited nodes.
    Returns the first node encountered twice, identifying the loop start.
    """
    visited = set()
    current = head

    while current:
        if current in visited:
            return current
        visited.add(current)
        current = current.next

    return None

# Driver code to test both methods
if __name__ == "__main__":
    head = create_sample_linked_list_with_loop()

    loop_start_floyd = find_loop_start_floyd(head)
    if loop_start_floyd:
        print("Floyd’s Method - Loop starts at node with value:", loop_start_floyd.val)
    else:
        print("Floyd’s Method - No loop detected")

    loop_start_visited = find_loop_start_visited(head)
    if loop_start_visited:
        print("Visited Nodes Method - Loop starts at node with value:", loop_start_visited.val)
    else:
        print("Visited Nodes Method - No loop detected")
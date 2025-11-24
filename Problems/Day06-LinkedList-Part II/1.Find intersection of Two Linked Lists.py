# LeetCode Problem URL: https://leetcode.com/problems/intersection-of-two-linked-lists/
#
# Problem Description:
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.
#
# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
#
# Example 2:
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
#
# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
#
# Constraints:
# - The number of nodes of listA is m.
# - The number of nodes of listB is n.
# - 1 <= m, n <= 3 * 10^4
# - 1 <= Node.val <= 10^5
# - 0 <= skipA <= m
# - 0 <= skipB <= n
# - intersectVal is 0 if there is no intersected node.
# - intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
#
# Follow up: Write a solution that runs in O(m + n) time and uses only O(1) memory.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#########################################################
# Approach 0: Brute Force O(m * n)
# Time Complexity: O(m * n)
# Space Complexity: O(1)
#########################################################
class Solution:
    def getIntersectionNode_brute_force(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Brute Force (Nested Loops):
        1. For each node in List A, traverse List B to check if any node matches by reference.
        2. If a matching node is found, that's the intersection.
        3. Otherwise, return None.
        """
        currA = headA
        while currA:
            currB = headB
            while currB:
                if currA == currB:
                    return currA
                currB = currB.next
            currA = currA.next
        return None

#########################################################
# Approach 1: Hash Set (store references from one list)
# Time Complexity: O(m + n)
# Space Complexity: O(m)
#########################################################
    def getIntersectionNode_hash(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Hash Set approach:
        1. Traverse list A and store each node reference in a set.
        2. Traverse list B and check if any node is in the set.
        3. The first such node found is the intersection.
        """
        visited = set()
        curr = headA
        while curr:
            visited.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in visited:
                return curr
            curr = curr.next
        return None

#########################################################
# Approach 2: Length Calculation and Two Pointer Advance
# Time Complexity: O(m + n)
# Space Complexity: O(1)
#########################################################
    def getIntersectionNode_length(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Two Pointer approach:
        1. Calculate length of both lists.
        2. Advance pointer of longer list by length diff.
        3. Move both pointers together, checking for intersection.
        """
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        lenA = get_length(headA)
        lenB = get_length(headB)
        pa, pb = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                pa = pa.next
        else:
            for _ in range(lenB - lenA):
                pb = pb.next
        while pa and pb:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None

#########################################################
# Approach 3: Constant-space Two Pointer (Pointer Switching)
# Time Complexity: O(m + n)
# Space Complexity: O(1)
#########################################################
    def getIntersectionNode_pointer_switch(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Pointer switching approach:
        1. Initialize two pointers pa and pb at headA, headB.
        2. Traverse both, moving to other list's head when reaching end.
        3. They meet at intersection or both at None (no intersection).
        """
        if not headA or not headB:
            return None
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa

#########################################################
# Example Initialization and Demo Run
#########################################################
def build_linked_lists():
    """
    Builds two linked lists that intersect:
    A: 4 -> 1 -> 8 -> 4 -> 5
    B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    Intersected at node with value 8
    """
    # Shared part
    intersect = ListNode(8)
    intersect.next = ListNode(4)
    intersect.next.next = ListNode(5)
    # List A
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = intersect
    # List B
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = intersect
    return headA, headB

if __name__ == "__main__":
    headA, headB = build_linked_lists()
    sol = Solution()
    print("Brute Force approach intersection node value:")
    ans = sol.getIntersectionNode_brute_force(headA, headB)
    print(ans.val if ans else None)

    print("\nHash Set approach intersection node value:")
    ans = sol.getIntersectionNode_hash(headA, headB)
    print(ans.val if ans else None)

    print("\nLength difference approach intersection node value:")
    ans = sol.getIntersectionNode_length(headA, headB)
    print(ans.val if ans else None)

    print("\nPointer switching approach intersection node value:")
    ans = sol.getIntersectionNode_pointer_switch(headA, headB)
    print(ans.val if ans else None)

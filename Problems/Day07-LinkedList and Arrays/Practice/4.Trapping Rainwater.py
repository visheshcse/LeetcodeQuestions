"""
Question URL:
LeetCode: https://leetcode.com/problems/trapping-rain-water/

Question Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""

def trap_bruteforce(height):
    """
    Brute Force Approach
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Steps:
    1. For each element, find the highest wall to the left and right.
    2. Water at current index is min(left_max, right_max) - height[i] if that is positive.
    3. Sum this for all bars.
    """
   
def trap_dynamic(height):
    """
    Dynamic Programming / Precomputed Arrays Approach
    Time Complexity: O(n)
    Space Complexity: O(n)

    Steps:
    1. Precompute left_max for each bar.
    2. Precompute right_max for each bar.
    3. Water at each position i is min(left_max[i], right_max[i]) - height[i].
    4. Sum for all positions.
    """
    

def trap_stack(height):
    """
    Monotonic Stack Approach
    Time Complexity: O(n)
    Space Complexity: O(n)

    Steps:
    1. Use a stack to keep the indices of decreasing bars.
    2. When you encounter a higher bar, start popping.
    3. For every popped bar, compute the water trapped with the left and right boundary.
    """
    

def trap_two_pointers(height):
    """
    Two Pointers Approach
    Time Complexity: O(n)
    Space Complexity: O(1)

    Steps:
    1. Use two pointers at the beginning and end of the array.
    2. Keep track of the maximum wall to the left and right.
    3. Move the pointer with smaller value inward, accumulating water trapped.
    """
    

if __name__ == "__main__":
    # Sample input
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("Elevation map:", height)

    print("\nBrute Force Solution:")
    print(trap_bruteforce(height))

    print("\nDynamic Programming (Precomputed arrays) Solution:")
    print(trap_dynamic(height))

    print("\nStack Solution:")
    print(trap_stack(height))

    print("\nTwo Pointers Solution:")
    print(trap_two_pointers(height))

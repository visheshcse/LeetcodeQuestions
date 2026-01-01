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
    n = len(height)
    water = 0
    for i in range(n):
        left_max = 0
        right_max = 0
        
        # Scan left
        for j in range(i, -1, -1):
            left_max = max(left_max, height[j])
        # Scan right
        for j in range(i, n):
            right_max = max(right_max, height[j])
        
        water += min(left_max, right_max) - height[i]
    return water

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
    if not height:
        return 0

    n = len(height)
    water = 0
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]
    return water

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
    n = len(height)
    water = 0
    stack = []

    for i in range(n):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[top]
            water += distance * bounded_height
        stack.append(i)
    return water

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
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

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

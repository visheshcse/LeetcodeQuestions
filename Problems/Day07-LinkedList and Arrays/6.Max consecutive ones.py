"""
Question URL:
LeetCode: https://leetcode.com/problems/max-consecutive-ones/

Question Description:
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
"""

def findMaxConsecutiveOnes(nums):
    """
    Optimal One Pass Approach
    Time Complexity: O(n)
    Space Complexity: O(1)

    Steps:
    1. Initialize max_count and current_count to zero.
    2. Traverse array from left to right:
        - If nums[i] == 1, increment current_count.
        - If nums[i] == 0, reset current_count to zero.
        - Update max_count as needed.
    3. Return max_count (maximum sequence length of consecutive 1's).
    """
    max_count, current_count = 0, 0
    for n in nums:
        if n == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count

if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    print("Input array:", nums)
    print("Max consecutive ones:", findMaxConsecutiveOnes(nums))

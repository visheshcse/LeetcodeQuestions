"""
Question URL:
LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Question Description:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things: 
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
- Return k.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k.
"""

def removeDuplicates_bruteforce(nums):
    """
    Brute Force Approach (Not in-place, for clarity)
    Time Complexity: O(n)
    Space Complexity: O(n)

    Steps:
    1. Use a set to collect unique elements.
    2. Place them at the beginning of the nums array in original order.
    3. Fill rest of array (if any) with underscores.
    4. Return number of unique elements.
    """
    unique = []
    prev = None
    for n in nums:
        if n != prev:
            unique.append(n)
            prev = n
    for i in range(len(unique)):
        nums[i] = unique[i]
    for i in range(len(unique), len(nums)):
        nums[i] = '_'   # Using '_' to indicate irrelevant slots
    return len(unique)

def removeDuplicates_twopointer(nums):
    """
    Two Pointer Approach (Official Solution)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Steps:
    1. Use two pointers: 'slow' for the position of the next unique element, 'fast' for the current index.
    2. Traverse the array with fast; whenever nums[fast] != nums[slow], increment slow and copy nums[fast].
    3. After traversal, slow + 1 is the count of unique elements. The array's first (slow + 1) elements are the answer.
    4. Rest of array is left unchanged.
    """
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    for i in range(slow + 1, len(nums)):
        nums[i] = '_'
    return slow + 1

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 4, 4, 5]
    print("Original array:", nums)

    print("\nBrute Force Approach (for understanding, not in-place):")
    nums_bf = nums.copy()
    k1 = removeDuplicates_bruteforce(nums_bf)
    print(f"Unique count: {k1}")
    print("Result array:", nums_bf)

    print("\nOptimal Two Pointer Approach:")
    nums_tp = nums.copy()
    k2 = removeDuplicates_twopointer(nums_tp)
    print(f"Unique count: {k2}")
    print("Result array:", nums_tp)

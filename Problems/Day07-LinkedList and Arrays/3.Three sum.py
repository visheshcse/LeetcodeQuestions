"""
LeetCode URL: https://leetcode.com/problems/3sum/

Question Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

#########################################################
# Brute Force Approach: Triple Nested Loops
#########################################################

def threeSum_brute(nums):
    """
    Time Complexity: O(N^3)
    Space Complexity: O(N) for output storage
    
    Algorithm Steps:
    1. Iterate over all triplets (i, j, k) with three nested loops.
    2. Check if the sum of nums[i], nums[j], nums[k] is zero.
    3. Keep the triplets in a set to avoid duplicates.
    4. Convert the set to a list before returning.
    """
    n = len(nums)
    res = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    res.add(triplet)
    return list(res)

#########################################################
# Better Approach (Take U Forward Reference): Fix two elements + hash set for third element (no sorting)
#########################################################

def threeSum_better(nums):
    """
    Time Complexity: O(N^2)
    Space Complexity: O(N) for hash set and output storage
    
    Algorithm Steps:
    1. Iterate for first element i.
    2. Iterate for second element j > i.
    3. Calculate target = -(nums[i] + nums[j]).
    4. Use a hash set to check if target is present among remaining elements.
    5. Use a set to store unique triplets (sorted tuples) to avoid duplicates.
    """
    n = len(nums)
    res = set()
    for i in range(n):
        seen = set()
        for j in range(i + 1, n):
            target = -(nums[i] + nums[j])
            if target in seen:
                triplet = tuple(sorted((nums[i], nums[j], target)))
                res.add(triplet)
            seen.add(nums[j])
    return list(res)

#########################################################
# Optimized Approach: Sorting + Two Pointer + Skip Duplicates
#########################################################

def threeSum_optimized(nums):
    """
    Time Complexity: O(N^2)
    Space Complexity: O(N) for sorting and output storage
    
    Algorithm Steps:
    1. Sort the array.
    2. Iterate with index i, skipping duplicates.
    3. Use two pointers left = i+1 and right = n-1.
    4. Move pointers based on sum compared with zero while skipping duplicates.
    5. Add valid triplets to result list.
    """
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res


#########################################################
# Sample Initialization and Execution
#########################################################

sample_nums = [-1, 0, 1, 2, -1, -4]

print("Input Array:", sample_nums)

print("
Brute Force Approach Output:")
print(threeSum_brute(sample_nums))

print("
Better Approach Output (Take U Forward Reference):")
print(threeSum_better(sample_nums))

print("
Optimized Approach Output:")
print(threeSum_optimized(sample_nums))
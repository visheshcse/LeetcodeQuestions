# LeetCode Problem URL: https://leetcode.com/problems/subsets-ii/
#
# Problem Description:
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Example 1:
# Input: nums = [1,2,2]
# Output: [[], [1], [2], [1,2], [1,2,2], [2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[], [0]]
#
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
#
# Editorial Approaches included:
# 1. Backtracking (with duplicate skipping)
# 2. Iterative (simulate DP/enumeration with duplicate handling)
# 3. Bitmasking (with deduplication)

from typing import List

############################################
# Approach 1: Backtracking (with duplicate skipping)
# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * 2^N)
############################################
class Solution:
    def subsetsWithDup_backtracking(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking approach with duplicate skipping:
        1. Sort the array to group duplicates.
        2. Use DFS to recursively build subsets.
        3. At each recursive call, skip duplicate elements.
        4. Add a copy of the path to result at every call.
        """
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        nums.sort()
        result = []
        backtrack(0, [])
        return result

############################################
# Approach 2: Iterative (Sort and simulate subsets expansion, handle duplicates)
# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * 2^N)
############################################
    def subsetsWithDup_iterative(self, nums: List[int]) -> List[List[int]]:
        """
        Iterative approach:
        1. Sort the array to bring duplicates together.
        2. Use a result list that is expanded at each step.
        3. To handle duplicates, only expand subsets generated in last step.
        """
        nums.sort()
        result = [[]]
        last_size = 0  # Track size of previous expansion for duplicates
        for i, num in enumerate(nums):
            # If duplicate, do not use all previous results, only those added in previous step
            if i > 0 and nums[i] == nums[i - 1]:
                start = last_size
            else:
                start = 0
            last_size = len(result)
            for j in range(start, last_size):
                result.append(result[j] + [num])
        return result

############################################
# Approach 3: Bitmasking (with deduplication using set)
# Time Complexity: O(N * 2^N), but extra due to set operations
# Space Complexity: O(N * 2^N)
############################################
    def subsetsWithDup_bitmask(self, nums: List[int]) -> List[List[int]]:
        """
        Bitmasking approach:
        1. Each bitmask (0 to 2^n-1) represents element selection.
        2. Store each generated subset as a tuple in a set to ensure uniqueness.
        3. Sort array to handle duplicate elements properly.
        """
        nums.sort()
        n = len(nums)
        seen = set()
        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            seen.add(tuple(subset))
        return [list(t) for t in seen]

############################################
# Sample Input Initialization and Demo Run
############################################
if __name__ == "__main__":
    nums = [1, 2, 2]

    sol = Solution()
    print("Backtracking approach output:")
    print(sorted(sol.subsetsWithDup_backtracking(nums)))

    print("\nIterative approach output:")
    print(sorted(sol.subsetsWithDup_iterative(nums)))

    print("\nBitmasking approach output:")
    print(sorted(sol.subsetsWithDup_bitmask(nums)))

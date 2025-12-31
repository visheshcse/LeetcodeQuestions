# LeetCode Problem URL: https://leetcode.com/problems/subsets/
# Problem Description:
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Example:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List

class Solution:
    ########################################
    # Approach 1: Brute Force (Iterative)
    # Time Complexity: O(N * 2^N), N is length of nums
    # Space Complexity: O(N * 2^N) for output storage
    ########################################
    def subsets_brute_force(self, nums: List[int]) -> List[List[int]]:
        """
        Brute Force approach:
        - Generate all subsets by iterating over existing subsets and adding current num to them.
        - Start with empty subset and expand by including each number.
        """
        result = [[]]  # Start with empty subset
        for num in nums:
            # Take all existing subsets and add current number to form new subsets
            new_subsets = [curr + [num] for curr in result]
            result.extend(new_subsets)
        return result

    ########################################
    # Approach 2: Backtracking (DFS)
    # Time Complexity: O(N * 2^N)
    # Space Complexity: O(N * 2^N) for recursion stack and output
    ########################################
    def subsets_backtracking(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking approach:
        - Use DFS to explore choices: to include or exclude each element.
        - Maintain a current path and add to result at each step.
        """
        def backtrack(start, path):
            # Add a copy of current path as a subset
            result.append(path[:])
            for i in range(start, len(nums)):
                # Include nums[i]
                path.append(nums[i])
                backtrack(i + 1, path)
                # Backtrack: remove last element before next iteration
                path.pop()

        result = []
        backtrack(0, [])
        return result
    
    def subsets_backtracking_two_calls(nums):
        """
        Backtracking with two recursion calls:
        At each index, recursively explore both:
        - Including nums[index]
        - Excluding nums[index]
        Time Complexity: O(N * 2^N)
        Space Complexity: O(N * 2^N)
        """
        result = []

        def dfs(index, path):
            if index == len(nums):
                result.append(path[:])  # reached end, add current subset
                return
            # Decision 1: exclude nums[index]
            dfs(index + 1, path)
            # Decision 2: include nums[index]
            dfs(index + 1, path + [nums[index]])

        dfs(0, [])
        return result


    ########################################
    # Approach 3: Bitmasking
    # Time Complexity: O(N * 2^N)
    # Space Complexity: O(N * 2^N)
    ########################################
    def subsets_bitmask(self, nums: List[int]) -> List[List[int]]:
        """
        Bitmasking approach:
        - Use bitmask from 0 to 2^N - 1 to represent subsets.
        - For each bitmask, include elements corresponding to set bits.
        """
        n = len(nums)
        result = []
        for mask in range(1 << n):  # from 0 to 2^n -1
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            result.append(subset)
        return result


if __name__ == "__main__":
    # Sample Input Initialization
    nums = [1, 2, 3]

    sol = Solution()

    # Run and print output for each approach
    print("Brute Force Approach Output:")
    print(sol.subsets_brute_force(nums))

    print("\nBacktracking Approach Output:")
    print(sol.subsets_backtracking(nums))

    print("\nDynamic Programming Approach Output:")
    print(sol.subsets_dp(nums))

    print("\nBitmasking Approach Output:")
    print(sol.subsets_bitmask(nums))

# LeetCode Problem URL: https://leetcode.com/problems/combination-sum/
#
# Problem Description:
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
#
# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
#
# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#
# Example 3:
# Input: candidates = [2], target = 1
# Output: []
#
# Constraints:
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

from typing import List

#############################################################
# Approach 1: Backtracking (DFS with pruning)
# Time Complexity: O(2^(target/min(candidates)) * k)
#   - For each number up to target, we may branch recursively, pruning when sum exceeds target.
# Space Complexity: O(target/min(candidates)) for recursion stack and output (can be exponential)
#############################################################

class Solution:
    def combinationSum_backtracking(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking solution:
        1. Sort the candidates (optional, but helps with understanding/pruning).
        2. Use recursive DFS to choose each number 0..n times (unlimited uses).
        3. At each call, try each candidate from current index onward (avoid permutations).
        4. If the sum exceeds the target, prune/return.
        5. If sum == target, add the current combination to the result.
        """
        def dfs(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # Use i (not i+1) because we can reuse the same element
                dfs(i, path, total + candidates[i])
                path.pop()

        result = []
        candidates.sort()
        dfs(0, [], 0)
        return result

#############################################################
# Approach 2: Dynamic Programming (Tabulation - Bottom Up)
# Time Complexity: O(target * len(candidates)) per solution generated
# Space Complexity: O(target * k) where k is average number of combinations for target
#############################################################

    def combinationSum_dp(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        DP Tabulation solution:
        1. dp[t] will store a list of combinations that sum up to t.
        2. For each candidate and each t from candidate to target,
           extend combinations in dp[t - candidate] by adding candidate.
        3. At the end, dp[target] has all solutions.
        """
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for candidate in candidates:
            for t in range(candidate, target + 1):
                for comb in dp[t - candidate]:
                    dp[t].append(comb + [candidate])
        return dp[target]

#############################################################
# Approach 3: Backtracking (choose or don't choose at index)
# Time Complexity: O(2^N * k)
# Space Complexity: O(target * k)
#############################################################

    def combinationSum_recursive_pick_skip(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Alternative recursive solution showing binary choice at each index:
        - At each step, decide whether to pick the current candidate (and stay on it)
          or skip it and move to the next one.
        """
        def helper(idx, current, total):
            if total == target:
                result.append(current[:])
                return
            if total > target or idx >= len(candidates):
                return
            # Case 1: Pick current candidate
            current.append(candidates[idx])
            helper(idx, current, total + candidates[idx])
            current.pop()
            # Case 2: Skip current candidate
            helper(idx + 1, current, total)

        result = []
        candidates.sort()
        helper(0, [], 0)
        return result

#############################################################
# Sample Initialization and Demonstration
#############################################################
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7

    sol = Solution()
    print("Backtracking approach output:")
    print(sol.combinationSum_backtracking(candidates, target))

    print("\nDP Tabulation approach output:")
    print(sol.combinationSum_dp(candidates, target))

    print("\nRecursive Pick/Skip approach output:")
    print(sol.combinationSum_recursive_pick_skip(candidates, target))

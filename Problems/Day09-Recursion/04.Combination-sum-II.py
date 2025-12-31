# LeetCode Problem URL: https://leetcode.com/problems/combination-sum-ii/
#
# Problem Description:
# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
#
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
#
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: [[1,2,2],[5]]
#
# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

from typing import List

###############################################################
# Approach 1: Backtracking (with duplicate skipping)
# Time Complexity: O(2^N) (in worst case, must explore every pick/skip possibility)
# Space Complexity: O(N) for recursion stack, plus storage for solutions
###############################################################

class Solution:
    def combinationSum2_backtracking(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking with duplicate skipping:
        1. Sort candidates to group duplicates.
        2. At each recursion, iterate through elements (i -> n).
        3. If current candidate equals previous candidate and previous was not picked (at same recursion level), skip.
        4. If sum target reached, add path to result.
        5. At each call, do not revisit previous elements (only move forward!).
        """
        def dfs(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            prev = None
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # Skip duplicate numbers at the same tree depth
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()
                prev = candidates[i]

        candidates.sort()
        result = []
        dfs(0, [], 0)
        return result

###############################################################
# Approach 2: Iterative (Simulated DP/expansion with duplicate check)
# Time Complexity: O(2^N)
# Space Complexity: O(N) for subset storage
###############################################################
    def combinationSum2_iterative(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Iterative subset simulation:
        1. Sort candidates for deduplication.
        2. Use an expanding list of [current combination, remaining sum, index].
        3. If remaining sum == 0, add combination to result.
        4. For each candidate, only use next index (advance, as each can be used once).
        5. Skip duplicates at the same index.
        """
        candidates.sort()
        result = []
        stack = [([], target, 0)]
        while stack:
            path, rem, start = stack.pop()
            if rem == 0:
                result.append(path)
                continue
            prev = None
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                if candidates[i] > rem:
                    break
                stack.append((path + [candidates[i]], rem - candidates[i], i + 1))
                prev = candidates[i]
        return result

###############################################################
# Approach 3: Backtracking (pick/skip, passing last picked index)
# Time Complexity: O(2^N)
# Space Complexity: O(N)
###############################################################
    def combinationSum2_pick_skip(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Pick/skip recursive approach:
        1. Sort, recurse: at each idx, pick element (move to next) or skip duplicates.
        2. Skip duplicate candidates at any index after picking.
        3. If target == 0, add combination. If target < 0 or end, backtrack.
        """
        def helper(idx, path, rem):
            if rem == 0:
                result.append(path[:])
                return
            if rem < 0 or idx == len(candidates):
                return
            # Pick idx
            path.append(candidates[idx])
            helper(idx + 1, path, rem - candidates[idx])
            path.pop()
            # Skip further duplicate candidates
            nxt = idx + 1
            while nxt < len(candidates) and candidates[nxt] == candidates[idx]:
                nxt += 1
            helper(nxt, path, rem)

        candidates.sort()
        result = []
        helper(0, [], target)
        return result

###############################################################
# Sample Initialization and Demonstration
###############################################################
if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8

    sol = Solution()
    print("Backtracking approach output:")
    print(sorted(sol.combinationSum2_backtracking(candidates, target)))

    print("\nIterative approach output:")
    print(sorted(sol.combinationSum2_iterative(candidates, target)))

    print("\nBacktracking pick/skip output:")
    print(sorted(sol.combinationSum2_pick_skip(candidates, target)))

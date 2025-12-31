# LeetCode Problem URL: https://leetcode.com/problems/palindrome-partitioning/
#
# Problem Description:
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s. [page:0]
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]] [page:0]
#
# Example 2:
# Input: s = "a"
# Output: [["a"]] [page:0]
#
# Constraints:
# - 1 <= s.length <= 16
# - s contains only lowercase English letters. [page:0]


from typing import List


class Solution:
    ########################################################
    # Approach 1: Backtracking with On-the-fly Palindrome Check
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n)
    ########################################################
    def partition_backtracking(self, s: str) -> List[List[str]]:
        """
        Backtracking (DFS) approach:
        1. Use recursion to try all possible partitions by cutting the string
           at every index from 'start' to end.
        2. At each step, for substring s[start:i+1], check if it is a palindrome.
        3. If it is, append it to the current path and recurse from i+1.
        4. When start reaches len(s), add the current path as one valid partition.

        Time Complexity: O(n * 2^n)
        - There are 2^(n-1) ways to partition positions and each step may involve
          palindrome checking up to O(n).
        Space Complexity: O(n)
        - Recursion depth up to n and current path storing at most n substrings.
        """
        result = []
        n = len(s)

        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start: int, path: List[str]) -> None:
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if is_palindrome(start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return result

    ########################################################
    # Approach 2: Backtracking + DP Palindrome Table
    # Time Complexity: O(n^2 + 2^n * n)
    # Space Complexity: O(n^2)
    ########################################################
    def partition_dp_backtracking(self, s: str) -> List[List[str]]:
        """
        Backtracking with Dynamic Programming palindrome table:
        1. Precompute a 2D DP table 'is_pal[i][j]' that stores whether s[i:j+1] is a palindrome.
           - Fill bottom-up using:
             - is_pal[i][i] = True
             - is_pal[i][j] = (s[i]==s[j]) and (j-i<=2 or is_pal[i+1][j-1])
        2. Use DFS/backtracking similar to approach 1, but check palindromes
           in O(1) using the DP table instead of re-checking characters.
        3. When start reaches len(s), push the built path to result.

        Time Complexity:
        - O(n^2) to build DP table.
        - O(2^n * n) in worst case for exploring partitions.
        Space Complexity:
        - O(n^2) DP table plus O(n) recursion/path space.
        """
        n = len(s)
        # 1) Build DP palindrome table
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        result = []

        def dfs(start: int, path: List[str]) -> None:
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if is_pal[start][end]:
                    path.append(s[start:end + 1])
                    dfs(end + 1, path)
                    path.pop()

        dfs(0, [])
        return result

    ########################################################
    # Approach 3: Backtracking with Growing Substring (Your Variant)
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n)
    ########################################################
    def partition_growing_substring(self, s: str) -> List[List[str]]:
        """
        Backtracking with growing substring:
        1. Traverse string with index i and a 'curr' substring being built.
        2. At each character s[i], extend curr = curr + s[i].
        3. If curr is a palindrome:
           - Option A: "cut" here, push curr into path and recurse from i+1
             with curr reset to "".
        4. Option B: regardless of palindrome or not, also recurse to i+1
           with curr extended (no cut).
        5. When i reaches len(s), only accept partitions where curr == "".

        Time Complexity: O(n * 2^n)
        - Each character can either cause a cut or be merged into a larger piece.
        - O(2^n) states / solutions (because of the branching).
        - O(n) work per solution to copy substrings and paths.(basically substring operations like this - curr_new = curr + s[i])
        Space Complexity: O(n)
        - Recursion depth up to n and current path.
        """
        res: List[List[str]] = []
        n = len(s)

        def backtrack(i: int, path: List[str], curr: str) -> None:
            if i == n:
                if curr == "":
                    res.append(path[:])
                return

            curr_new = curr + s[i]

            # Option A: cut here if palindrome
            if curr_new == curr_new[::-1]:
                path.append(curr_new)
                backtrack(i + 1, path, "")
                path.pop()

            # Option B: extend further without cutting
            backtrack(i + 1, path, curr_new)

        backtrack(0, [], "")
        return res


########################################################
# Demo run
########################################################
if __name__ == "__main__":
    sol = Solution()

    s = "aab"
    print("Backtracking approach:")
    print(f's="{s}" ->', sol.partition_backtracking(s))

    print("DP + Backtracking approach:")
    print(f's="{s}" ->', sol.partition_dp_backtracking(s))

    print("Growing-substring backtracking approach:")
    print(f's="{s}" ->', sol.partition_growing_substring(s))

    s = "a"
    print("Backtracking approach:")
    print(f's="{s}" ->', sol.partition_backtracking(s))

    print("DP + Backtracking approach:")
    print(f's="{s}" ->', sol.partition_dp_backtracking(s))

    print("Growing-substring backtracking approach:")
    print(f's="{s}" ->', sol.partition_growing_substring(s))

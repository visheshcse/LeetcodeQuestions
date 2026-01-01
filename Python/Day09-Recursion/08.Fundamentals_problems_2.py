"""
Chai aur Recursion — LeetCode Implementations (Python)

This single file contains LeetCode-acceptable `Solution` classes for
the main recursion/backtracking problems discussed in the video: [web:38][web:34][web:40][web:41]

1) Count Good Numbers (LeetCode 1922)
   https://leetcode.com/problems/count-good-numbers/ [web:38]

2) Generate Parentheses (LeetCode 22)
   https://leetcode.com/problems/generate-parentheses/ [web:34]

3) Letter Combinations of a Phone Number (LeetCode 17)
   https://leetcode.com/problems/letter-combinations-of-a-phone-number/ [web:40]

4) Combination Sum – prune approach (LeetCode 39)
   https://leetcode.com/problems/combination-sum/ [web:41]

You cannot submit them together on LeetCode, but this is convenient
for local practice and reference.
"""

from typing import List


# ---------------------------------------------------------------------------
# 1) Count Good Numbers – LeetCode 1922
# ---------------------------------------------------------------------------

class SolutionCountGoodNumbers:
    def countGoodNumbers(self, n: int) -> int:
        """
        Count Good Numbers - LeetCode 1922

        TIME:  O(log n) using fast exponentiation
        SPACE: O(1)

        A digit string of length n is "good" if:
          - Even indices (0-based) have even digits: {0,2,4,6,8} (5 choices)
          - Odd indices have prime digits: {2,3,5,7} (4 choices)

        Let even_positions = ceil(n/2), odd_positions = floor(n/2).
        Answer = 5^even_positions * 4^odd_positions (mod 1e9+7). [web:38]
        """
        MOD = 10**9 + 7
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD


# ---------------------------------------------------------------------------
# 2) Generate Parentheses – LeetCode 22
# ---------------------------------------------------------------------------

class SolutionGenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate Parentheses - LeetCode 22

        TIME:  O(C_n * n), C_n = nth Catalan number
        SPACE: O(n) recursion stack + O(C_n * n) output

        Backtracking with pruning:
          - Track open_used, close_used, and current string.
          - Add '(' if open_used < n.
          - Add ')' if close_used < open_used.
          - When open_used == close_used == n, add to answer. [web:34]
        """
        res: List[str] = []

        def backtrack(open_used: int, close_used: int, curr: str) -> None:
            if open_used == n and close_used == n:
                res.append(curr)
                return

            if open_used < n:
                backtrack(open_used + 1, close_used, curr + "(")

            if close_used < open_used:
                backtrack(open_used, close_used + 1, curr + ")")

        backtrack(0, 0, "")
        return res


# ---------------------------------------------------------------------------
# 3) Letter Combinations of a Phone Number – LeetCode 17
# ---------------------------------------------------------------------------

class SolutionLetterCombinations:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Letter Combinations of a Phone Number - LeetCode 17

        TIME:  O(4^n * n) in worst case (digits 7/9 give 4 letters)
        SPACE: O(4^n) recursion tree + output

        Backtracking:
          - If digits is empty, return [].
          - Map each digit 2–9 to its letters.
          - DFS(index, path):
             * When index == len(digits), append path.
             * Otherwise, iterate letters for digits[index] and recurse. [web:40]
        """
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res: List[str] = []

        def backtrack(i: int, path: str) -> None:
            if i == len(digits):
                res.append(path)
                return

            for ch in mapping[digits[i]]:
                backtrack(i + 1, path + ch)

        backtrack(0, "")
        return res


# ---------------------------------------------------------------------------
# 4) Combination Sum – LeetCode 39 (prune approach)
# ---------------------------------------------------------------------------

class SolutionCombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Combination Sum - LeetCode 39 (pruning backtracking)

        TIME:  Exponential in worst case; pruned when sum exceeds target
        SPACE: O(k) recursion depth + output

        Backtracking with pruning:
          1. Sort candidates.
          2. DFS(i, cur_sum, path):
             - If cur_sum == target: add copy of path.
             - If cur_sum > target or i == len(candidates): return.
          3. Choices at index i:
             a) Skip candidates[i]  -> DFS(i+1, cur_sum, path)
             b) Take candidates[i]  -> append; DFS(i, cur_sum + val); pop. [web:36][web:41]
        """
        candidates.sort()
        res: List[List[int]] = []
        n = len(candidates)

        def backtrack(i: int, cur_sum: int, path: List[int]) -> None:
            if cur_sum == target:
                res.append(path[:])
                return
            if cur_sum > target or i == n:
                return

            # Skip current
            backtrack(i + 1, cur_sum, path)

            # Take current
            path.append(candidates[i])
            backtrack(i, cur_sum + candidates[i], path)
            path.pop()

        backtrack(0, 0, [])
        return res


# ---------------------------------------------------------------------------
# Local demo / quick sanity checks
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Count Good Numbers (1922) ===")
    sc = SolutionCountGoodNumbers()
    print("n = 1  ->", sc.countGoodNumbers(1))
    print("n = 4  ->", sc.countGoodNumbers(4))
    print("n = 50 ->", sc.countGoodNumbers(50))
    print()

    print("=== Generate Parentheses (22) ===")
    sg = SolutionGenerateParenthesis()
    print("n = 3  ->", sg.generateParenthesis(3))
    print()

    print("=== Letter Combinations of a Phone Number (17) ===")
    sl = SolutionLetterCombinations()
    print('digits = "23" ->', sl.letterCombinations("23"))
    print()

    print("=== Combination Sum (39) ===")
    scs = SolutionCombinationSum()
    print("candidates = [2,3,6,7], target = 7 ->",
          scs.combinationSum([2, 3, 6, 7], 7))
    print("candidates = [2,3,5], target = 8 ->",
          scs.combinationSum([2, 3, 5], 8))

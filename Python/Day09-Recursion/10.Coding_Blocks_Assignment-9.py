from typing import List


# Merge Sort (helper-based, in-place using extra temp array)
# ------------------------------------------------------------

def merge_sort(arr: List[int]) -> None:
    """
    In-place merge sort (modifies arr).

    TIME:  O(n log n)
    SPACE: O(n) extra temp array
    """
    n = len(arr)
    if n <= 1:
        return

    temp = [0] * n

    def merge(l: int, m: int, r: int) -> None:
        i, j, k = l, m + 1, l
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1

        while i <= m:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j <= r:
            temp[k] = arr[j]
            j += 1
            k += 1

        for idx in range(l, r + 1):
            arr[idx] = temp[idx]

    def merge_sort_helper(l: int, r: int) -> None:
        if l >= r:
            return
        m = (l + r) // 2
        merge_sort_helper(l, m)
        merge_sort_helper(m + 1, r)
        merge(l, m, r)

    merge_sort_helper(0, n - 1)


# 1. Implement Quick Sort (recursive, helper-based)
# ------------------------------------------------------------

def quick_sort(arr: List[int]) -> None:
    """
    In-place Quick Sort using partition helper.

    TIME: Average O(n log n), worst O(n^2)
    SPACE: O(log n) recursion (in-place)
    """

    def partition(l: int, r: int) -> int:
        """
        Lomuto partition: choose arr[r] as pivot,
        place pivot in correct position and return its index.
        """
        pivot = arr[r]
        i = l - 1
        for j in range(l, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1

    def quick_sort_helper(l: int, r: int) -> None:
        if l < r:
            pi = partition(l, r)
            quick_sort_helper(l, pi - 1)
            quick_sort_helper(pi + 1, r)

    if len(arr) <= 1:
        return
    quick_sort_helper(0, len(arr) - 1)


# 2. Subsets that sum to N
# ------------------------------------------------------------

def subsets_sum_k(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all subsets (any size) whose sum is equal to target.
    TIME: O(2^n), SPACE: O(n) recursion + output
    """
    res: List[List[int]] = []
    n = len(nums)

    def backtrack(i: int, curr: List[int], curr_sum: int) -> None:
        if i == n:
            if curr_sum == target:
                res.append(curr[:])
            return

        # Exclude nums[i]
        backtrack(i + 1, curr, curr_sum)

        # Include nums[i]
        curr.append(nums[i])
        backtrack(i + 1, curr, curr_sum + nums[i])
        curr.pop()

    backtrack(0, [], 0)
    return res


# 3. Number -> all possible strings (1->A, 2->B, ..., 26->Z)
# ------------------------------------------------------------

def num_to_strings(num_str: str) -> List[str]:
    """
    Given a numeric string, print all possible strings
    mapping 1->A, ..., 26->Z.
    Example: "123" -> ["ABC", "AW", "LC"].
    TIME: O(2^n), SPACE: O(n)
    """
    res: List[str] = []
    n = len(num_str)

    def backtrack(i: int, path: str) -> None:
        if i == n:
            res.append(path)
            return

        # Take 1 digit
        val1 = int(num_str[i])
        if 1 <= val1 <= 26:
            backtrack(i + 1, path + chr(ord("A") + val1 - 1))

        # Take 2 digits
        if i + 1 < n:
            val2 = int(num_str[i : i + 2])
            if 1 <= val2 <= 26:
                backtrack(i + 2, path + chr(ord("A") + val2 - 1))

    backtrack(0, "")
    return res


# 4. Print all permutations of a string
# ------------------------------------------------------------

def permutations(s: str) -> List[str]:
    """
    Return all permutations of string s (assuming distinct chars).
    TIME: O(n! * n), SPACE: O(n) recursion + output
    """
    res: List[str] = []
    chars = list(s)
    n = len(chars)

    def backtrack(i: int) -> None:
        if i == n:
            res.append("".join(chars))
            return

        for j in range(i, n):
            chars[i], chars[j] = chars[j], chars[i]
            backtrack(i + 1)
            chars[i], chars[j] = chars[j], chars[i]

    backtrack(0)
    return res


# 5. Check if 'a'/'b' string follows the given rules
# ------------------------------------------------------------
# Rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'

def check_ab_string(s: str) -> bool:
    """
    Recursively check if s (only 'a' and 'b') follows the given rules.
    TIME: O(n), SPACE: O(n)
    """

    def helper(i: int) -> bool:
        if i == len(s):
            return True
        if s[i] != "a":
            return False
        if i == len(s) - 1:
            return True
        if s[i + 1] == "a":
            return helper(i + 1)
        if i + 2 < len(s) and s[i + 1] == "b" and s[i + 2] == "b":
            return helper(i + 3)
        return False

    if not s or s[0] != "a":
        return False
    return helper(0)


# 6. Output 1..N in string comparison order (lexicographical)
# ------------------------------------------------------------

def lexical_numbers(n: int) -> List[int]:
    """
    Output integers 1..n in lexicographical (string comparison) order.
    E.g. for n=13: [1,10,11,12,13,2,3,4,5,6,7,8,9].
    TIME: O(n), SPACE: O(n)
    """
    res: List[int] = []

    def dfs(curr: int) -> None:
        if curr > n:
            return
        if curr != 0:
            res.append(curr)
        start = 0 if curr != 0 else 1
        for d in range(start, 10):
            nxt = curr * 10 + d
            if nxt == 0:
                continue
            if nxt > n:
                break
            dfs(nxt)

    dfs(0)
    return res


# 7. Phone keypad combinations (digits -> words)
# ------------------------------------------------------------

def phone_keypad_combinations(digits: str) -> List[str]:
    """
    Using the phone keypad, return all possible words for input digits.
    Example: "23" -> ["ad","ae","af","bd","be","bf","cd","ce","cf"].
    TIME: O(4^n * n), SPACE: O(4^n)
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


# 8. Replace "pi" with "3.14" recursively
# ------------------------------------------------------------

def change_pi(s: str) -> str:
    """
    Recursively replace all "pi" with "3.14".
    Examples:
      change_pi("xpix") -> "x3.14x"
      change_pi("pipi") -> "3.143.14"
      change_pi("pip")  -> "3.14p"
    TIME: O(n), SPACE: O(n)
    """
    if len(s) < 2:
        return s
    if s[:2] == "pi":
        return "3.14" + change_pi(s[2:])
    return s[0] + change_pi(s[1:])


# ----------------------------------------------------------------
# Quick manual test
# ----------------------------------------------------------------

if __name__ == "__main__":
    a = [3, 6, 1, 5, 2, 4]
    merge_sort(a)
    print("Merge sort:", a)

    b = [3, 6, 1, 5, 2, 4]
    quick_sort(b)
    print("Quick sort:", b)

    print("Subsets sum to 5:", subsets_sum_k([1, 2, 3, 4], 5))
    print('Num to strings "123":', num_to_strings("123"))
    print("Permutations of 'abc':", permutations("abc"))
    print("Check 'abbabb':", check_ab_string("abbabb"))
    print("Lexical numbers up to 20:", lexical_numbers(20))
    print('Phone keypad "23":', phone_keypad_combinations("23"))
    print('change_pi("xpix"):', change_pi("xpix"))

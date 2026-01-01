from typing import List

# 1. Binary search (recursive)
# -------------------------------------------------------------------

def binary_search_recursive(arr: List[int], target: int, low: int, high: int) -> int:
    """
    Return index of target in sorted arr, or -1 if not found.
    TIME: O(log n), SPACE: O(log n) recursion
    """
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid - 1)
    return binary_search_recursive(arr, target, mid + 1, high)


# 2. Sum of array recursively
# -------------------------------------------------------------------

def sum_array_recursive(arr: List[int], i: int = 0) -> int:
    """
    Return sum of arr[i:].
    TIME: O(n), SPACE: O(n)
    """
    if i == len(arr):
        return 0
    return arr[i] + sum_array_recursive(arr, i + 1)


# 3. Check if array is sorted (ascending)
# -------------------------------------------------------------------

def is_sorted_recursive(arr: List[int], i: int = 0) -> bool:
    """
    Return True if arr is sorted in non-decreasing order.
    TIME: O(n), SPACE: O(n)
    """
    if i >= len(arr) - 1:
        return True
    if arr[i] > arr[i + 1]:
        return False
    return is_sorted_recursive(arr, i + 1)


# 4. Count number of zeros in an integer
# -------------------------------------------------------------------

def count_zeros(n: int) -> int:
    """
    Count digit '0' in the decimal representation of n.
    TIME: O(d), SPACE: O(d) where d = number of digits
    """
    n = abs(n)
    if n == 0:
        return 1  # if the number itself is 0, count one zero
    def helper(x: int) -> int:
        if x == 0:
            return 0
        return (1 if x % 10 == 0 else 0) + helper(x // 10)
    return helper(n)


# 5. Reverse a number using recursion
# -------------------------------------------------------------------

def reverse_number(n: int) -> int:
    """
    Reverse digits of integer n (sign preserved).
    TIME: O(d), SPACE: O(d)
    """
    sign = -1 if n < 0 else 1
    n = abs(n)

    def helper(x: int, acc: int) -> int:
        if x == 0:
            return acc
        return helper(x // 10, acc * 10 + x % 10)

    return sign * helper(n, 0)


# 6. Reverse a string using recursion
# -------------------------------------------------------------------

def reverse_string_recursive(s: str) -> str:
    """
    Reverse string s.
    TIME: O(n), SPACE: O(n)
    """
    if len(s) <= 1:
        return s
    return reverse_string_recursive(s[1:]) + s[0]


# 7. Geometric sum: 1 + 1/2 + 1/4 + ... + 1/(2^k)
# -------------------------------------------------------------------

def geometric_sum(k: int) -> float:
    """
    Compute 1 + 1/2 + 1/4 + ... + 1/(2^k).
    TIME: O(k), SPACE: O(k)
    """
    if k == 0:
        return 1.0
    return geometric_sum(k - 1) + 1 / (2 ** k)


# 8. Check if one string is reverse of the other
# -------------------------------------------------------------------

def is_reverse(a: str, b: str) -> bool:
    """
    Return True if b is reverse of a.
    TIME: O(n), SPACE: O(n)
    """
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True
    if a[0] != b[-1]:
        return False
    return is_reverse(a[1:], b[:-1])


# 9. Selection sort using recursion
# -------------------------------------------------------------------

def selection_sort_recursive(arr: List[int], i: int = 0) -> None:
    """
    In-place selection sort.
    TIME: O(n^2), SPACE: O(n)
    """
    n = len(arr)
    if i >= n - 1:
        return

    # find index of min element in arr[i:]
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    selection_sort_recursive(arr, i + 1)


# 10. Count all paths in MxN grid (only right or down)
# -------------------------------------------------------------------

def count_paths(m: int, n: int) -> int:
    """
    Count paths from top-left (0,0) to bottom-right (m-1,n-1) moving only right or down.
    TIME: O(m*n) with memo, SPACE: O(m*n)
    """
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def ways(i: int, j: int) -> int:
        if i == m - 1 and j == n - 1:
            return 1
        if i >= m or j >= n:
            return 0
        return ways(i + 1, j) + ways(i, j + 1)

    return ways(0, 0)


# 11. Remove consecutive duplicates from a string recursively
# -------------------------------------------------------------------

def remove_consecutive_duplicates(s: str) -> str:
    """
    Remove consecutive duplicate characters using tail recursion.
    Example: "aabccba" -> "abcba"

    TIME: O(n)
    SPACE: O(n) recursion stack + output (Python does not optimize tail calls)
    """
    def helper(i: int, acc: str) -> str:
        # i = current index, acc = result built so far
        if i == len(s):
            return acc

        # If acc is empty or current char differs from last char in acc, append it
        if not acc or s[i] != acc[-1]:
            acc += s[i]
        # else: skip s[i] because it's a consecutive duplicate

        return helper(i + 1, acc)  # tail call

    return helper(0, "")


# 12. Count ways to climb stairs with 1,2,3 steps
# -------------------------------------------------------------------

def count_ways_stairs(n: int) -> int:
    """
    Number of ways to climb n steps taking 1,2,3 at a time.
    TIME: O(n) with memo, SPACE: O(n)
    """
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def ways(k: int) -> int:
        if k == 0:
            return 1
        if k < 0:
            return 0
        return ways(k - 1) + ways(k - 2) + ways(k - 3)

    return ways(n)


# 13. Print all subsets of a string (using recursion)
# -------------------------------------------------------------------

def subsets_string(s: str) -> List[str]:
    """
    Return all non-empty subsets of string s.
    For "abc" -> ["a","b","c","ab","ac","bc","abc"].
    TIME: O(2^n * n), SPACE: O(2^n * n)
    """
    res: List[str] = []

    def backtrack(i: int, path: str) -> None:
        if i == len(s):
            if path:
                res.append(path)
            return
        # exclude s[i]
        backtrack(i + 1, path)
        # include s[i]
        backtrack(i + 1, path + s[i])

    backtrack(0, "")
    return res


# -------------------------------------------------------------------
# Quick manual test
# -------------------------------------------------------------------
if __name__ == "__main__":
    print("Binary search:", binary_search_recursive([1,2,3,4,5], 4, 0, 4))
    print("Sum array:", sum_array_recursive([1,2,3,4,5]))
    print("Is sorted:", is_sorted_recursive([1,2,2,5]))
    print("Count zeros:", count_zeros(1020300))
    print("Reverse number:", reverse_number(12345))
    print("Reverse string:", reverse_string_recursive("recursion"))
    print("Geometric sum k=3:", geometric_sum(3))
    print("Is reverse:", is_reverse("abc", "cba"))
    arr_test = [3,1,4,1,5]
    selection_sort_recursive(arr_test)
    print("Selection sort:", arr_test)
    print("Paths 3x3:", count_paths(3,3))
    print("Remove dup:", remove_consecutive_duplicates("aabccba"))
    print("Ways stairs n=4:", count_ways_stairs(4))
    print("Subsets of 'abc':", subsets_string("abc"))

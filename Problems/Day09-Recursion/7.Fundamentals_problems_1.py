"""
Basic Recursion and Loop Practice

This file contains small practice functions often used to build recursion
intuition (similar to early parts of recursion tutorials). [web:44]

Included functions:
1) print_numbers_recursive(start, end)
2) reverse_print_numbers_recursive(start, end)
3) sum_array_loop(arr)
4) sum_array_recursive(arr)
5) reverse_string_loop(s)
6) reverse_string_recursive(s)
7) factorial_loop(n)
8) factorial_recursive(n)

Each function documents its time and space complexity and core steps.
"""

from typing import List


# ---------------------------------------------------------------------------
# 1. Print numbers: recursive
# ---------------------------------------------------------------------------

def print_numbers_recursive(start: int, end: int) -> None:
    """
    Tail Recursion
    Print numbers from start to end (inclusive) using recursion.

    TIME:  O(n)  where n = max(0, end - start + 1)
    SPACE: O(n)  recursion stack

    Algorithm:
    1. Base case: if start > end, return.
    2. Print start.
    3. Recurse with start + 1.
    """
    if start > end:
        return
    print(start)
    print_numbers_recursive(start + 1, end)


# ---------------------------------------------------------------------------
# 2. Reverse print numbers: recursive
# ---------------------------------------------------------------------------

def reverse_print_numbers_recursive(start: int, end: int) -> None:
    """
    Head Recursion
    Print numbers from start to end (inclusive) in reverse using recursion.

    TIME:  O(n)  where n = max(0, end - start + 1)
    SPACE: O(n)  recursion stack

    Algorithm:
    1. Base case: if start > end, return.
    2. Recurse with start + 1.
    3. After recursion returns, print start.
    """
    if start > end:
        return
    reverse_print_numbers_recursive(start + 1, end)
    print(start)


# ---------------------------------------------------------------------------
# 3. Sum of array: loop
# ---------------------------------------------------------------------------

def sum_array_loop(arr: List[int]) -> int:
    """
    Sum all elements of an array using a loop.

    TIME:  O(n)
    SPACE: O(1)

    Algorithm:
    1. Set total = 0.
    2. For each element x in arr, add x to total.
    3. Return total.
    """
    total = 0
    for x in arr:
        total += x
    return total


# ---------------------------------------------------------------------------
# 4. Sum of array: recursive
# ---------------------------------------------------------------------------

def sum_array_recursive(arr: List[int], i: int = 0) -> int:
    """
    Sum all elements of an array using recursion.

    TIME:  O(n)
    SPACE: O(n) recursion stack

    Algorithm:
    1. Base case: if i == len(arr), return 0.
    2. Return arr[i] + sum_array_recursive(arr, i+1).
    """
    if i == len(arr):
        return 0
    return arr[i] + sum_array_recursive(arr, i + 1)


# ---------------------------------------------------------------------------
# 5. Reverse string: loop
# ---------------------------------------------------------------------------

def reverse_string_loop(s: str) -> str:
    """
    Reverse a string using a loop.

    TIME:  O(n)
    SPACE: O(n) for the new string

    Algorithm:
    1. Initialize empty list(chars).
    2. Iterate from end to start, append each character.
    3. Join chars as a new string and return.
    """
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return ''.join(chars)


# ---------------------------------------------------------------------------
# 6. Reverse string: recursive
# ---------------------------------------------------------------------------

def reverse_string_recursive(s: str) -> str:
    """
    Reverse a string using recursion.

    TIME:  O(n)
    SPACE: O(n) recursion stack + output

    Algorithm:
    1. Base case: if len(s) <= 1, return s.
    2. Return reverse_string_recursive(s[1:]) + s[0].
    """
    if len(s) <= 1:
        return s
    return reverse_string_recursive(s[1:]) + s[0]


# ---------------------------------------------------------------------------
# 7. Factorial: loop
# ---------------------------------------------------------------------------

def factorial_loop(n: int) -> int:
    """
    Compute n! using a loop (assumes n >= 0).

    TIME:  O(n)
    SPACE: O(1)

    Algorithm:
    1. Set result = 1.
    2. For i from 1 to n, multiply result by i.
    3. Return result.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ---------------------------------------------------------------------------
# 8. Factorial: recursive
# ---------------------------------------------------------------------------

def factorial_recursive(n: int) -> int:
    """
    Compute n! using recursion (assumes n >= 0).

    TIME:  O(n)
    SPACE: O(n) recursion stack

    Algorithm:
    1. Base case: if n == 0 or n == 1, return 1.
    2. Return n * factorial_recursive(n - 1).
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# ---------------------------------------------------------------------------
# Demo / Sample Runs
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== print_numbers_recursive(1, 5) ===")
    print_numbers_recursive(1, 5)
    print()

    print("=== reverse_print_numbers_recursive(1, 5) ===")
    reverse_print_numbers_recursive(1, 5)
    print()

    arr = [1, 2, 3, 4, 5]
    print("=== sum_array_loop([1,2,3,4,5]) ===")
    print(sum_array_loop(arr))
    print()

    print("=== sum_array_recursive([1,2,3,4,5]) ===")
    print(sum_array_recursive(arr))
    print()

    s = "recursion"
    print('=== reverse_string_loop("recursion") ===')
    print(reverse_string_loop(s))
    print()

    print('=== reverse_string_recursive("recursion") ===')
    print(reverse_string_recursive(s))
    print()

    print("=== factorial_loop(5) ===")
    print(factorial_loop(5))
    print()

    print("=== factorial_recursive(5) ===")
    print(factorial_recursive(5))

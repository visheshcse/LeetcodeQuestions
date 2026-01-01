"""
https://leetcode.com/problems/permutation-sequence/ [web:21]

Problem Description (LeetCode 60 - Permutation Sequence):
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132" 
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note: k is 1-indexed.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Constraints:
1 <= n <= 9
1 <= k <= n!
"""

class Solution:
    def brute_force_recursive(self, n: int, k: int) -> str:
        """
        Brute Force Recursive: Backtracking to generate permutations.
        
        SPACE: O(n! * n) - store all permutations in recursion stack + result
        TIME: O(n! * n) - generate all n! permutations recursively
        
        Algorithm Steps:
        1. Initialize empty result list and current path
        2. Recursive backtrack function:
           a. Base case: if path length == n, add to result
           b. For each unused number in 1..n:
              - Add to path
              - Recurse
              - Backtrack (remove)
        3. Sort result lexicographically
        4. Return (k-1)th permutation
        """
        nums = list(range(1, n + 1))
        result = []
        
        def backtrack(path, used):
            if len(path) == n:
                result.append(''.join(map(str, path)))
                return
            
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()
                    used[i] = False
        
        backtrack([], [False] * n)
        result.sort()
        return result[k - 1]
    
    def optimized(self, n: int, k: int) -> str:
        """
        Optimized Approach: Factorial Number System.
        
        SPACE: O(n) - available list + factorials
        TIME: O(n^2) - n positions, each pop O(n)
        
        Algorithm Steps:
        1. Precompute factorials: fact[i] = i!
        2. Create available numbers [1,2,...,n]
        3. Convert k to 0-indexed (k -= 1)
        4. For each position i from 0 to n-1:
           a. idx = k // fact[n-1-i]  (block index)
           b. Append available[idx] to result
           c. Remove available[idx]
           d. k = k % fact[n-1-i]     (next remainder)
        5. Join result into string
        
        Why it works: (n-i)! permutations start with each remaining digit.
        k//fact identifies which digit's block contains our permutation.
        """
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        
        available = list(range(1, n + 1))
        k -= 1  # 0-indexed
        result = []
        
        for i in range(n):
            fact_val = fact[n - 1 - i]
            idx = k // fact_val
            result.append(str(available.pop(idx)))
            k %= fact_val
        
        return ''.join(result)

# Initialize and test
if __name__ == "__main__":
    obj = Solution()
    
    # Test Case 1: n=3, k=3 → "213"
    print("Test 1 (n=3,k=3):")
    print("Brute Force Recursive:", obj.brute_force_recursive(3, 3))
    print("Optimized:            ", obj.optimized(3, 3))
    
    # Test Case 2: n=4, k=9 → "2314"
    print("\nTest 2 (n=4,k=9):")
    print("Brute Force Recursive:", obj.brute_force_recursive(4, 9))
    print("Optimized:            ", obj.optimized(4, 9))

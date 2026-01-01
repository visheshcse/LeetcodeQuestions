"""
Question URL:
LeetCode: https://leetcode.com/problems/3sum/

Question Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:
i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""


def threeSum_two_pointers(nums):
    """
    Two Pointers with Pre-Sort Approach
    Time Complexity: O(n^2)
    Space Complexity: O(n) due to result list

    Steps:
    1. Sort the input array.
    2. For each index i, use two pointers (left, right) to find pairs nums[l], nums[r] so that nums[i] + nums[l] + nums[r] == 0.
    3. Skip duplicates for nums[i], nums[l], nums[r] to ensure unique triplets.
    4. Collect valid triplets into output list.
    """
    length = len(nums)
    nums.sort()
    res = []
    for i in range(length):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = length-1
        while l < r:
            total = nums[i]+nums[l]+nums[r]
            if total == 0:
                res.append((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1

    return res


def threeSum_hashset_no_sort(nums):
    """
    HashSet No Sort Approach (Do not sort input, only sort triplet for set)
    Time Complexity: O(n^2)
    Space Complexity: O(n) for hashset and output

    Steps:
    1. For every i, use a hashset to store numbers seen after i.
    2. Search for pairs such that the complement forms a zero-sum with nums[i].
    3. Store each found triplet as a sorted tuple in set for uniqueness.
    4. Return list of lists from the set.
    """
    n = len(nums)
    res_set = set()
    for i in range(0,n):
        seen = set()
        for j in range(i+1, n):
            complement = -nums[i]-nums[j]
            if complement in seen:
                triplet = tuple(sorted([nums[i], nums[j], complement]))
                res_set.add(triplet)
            seen.add(nums[j])
    return res_set


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print("Sample Input:", nums)

    print("\nTwo Pointers with Pre-Sort Approach:")
    print(threeSum_two_pointers(nums))

    nums3 = [-1, 0, 1, 2, -1, -4]
    print("\nHashSet No Sort Approach (input not sorted):")
    print(threeSum_hashset_no_sort(nums3))

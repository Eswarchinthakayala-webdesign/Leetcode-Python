# Three Sum Problem

## Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

### Examples

**Example 1:**
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].


## Solution Approach

To solve this problem, we can use a combination of sorting and the two-pointer technique. Here are the steps in detail:

1. **Sort the Array**: Sorting helps in efficiently finding and avoiding duplicates.
2. **Iterate through the Array**: Fix one element and use two pointers to find the other two elements that sum up to zero.
3. **Use Two Pointers**: For the subarray to the right of the fixed element, use two pointers (left and right) to find pairs that sum to the negative of the fixed element.
4. **Check for Triplets**: If the sum of the three elements is zero, add the triplet to the result list. Move the pointers inward and skip duplicates.
5. **Avoid Duplicates**: Skip any duplicate elements to ensure all triplets are unique.
## Complexity Analysis
# Time Complexity: O(n^2)
Sorting the array takes O(n log n).
The main iteration and two-pointer search take O(n^2) in the worst case.
# Space Complexity: O(1) 
(excluding the space required for the output list).



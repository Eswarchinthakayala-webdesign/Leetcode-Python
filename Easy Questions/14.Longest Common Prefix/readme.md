# Longest Common Prefix

## Problem Description

Given an array of strings, write a function to find the longest common prefix string amongst the array of strings. If there is no common prefix, return an empty string `""`.

### Examples

**Example 1:**
Input: strs = ["flower","flow","flight"]
Output: "fl"

## Solution Approach

To solve the problem, we can use the following approach:

1. **Edge Case Handling**: If the input array is empty, return an empty string.
2. **Sort the Array**: Sorting the array helps in minimizing comparisons, as the smallest and largest string in lexicographical order will help determine the common prefix.
3. **Compare First and Last Strings**: Since the array is sorted, the common prefix of the first and last strings will be the common prefix for the entire array.

## Complexity Analysis
# Time Complexity:

Sorting the array takes O(n log n) time, where n is the number of strings in the array.
Comparing the first and last strings takes O(m) time, where m is the length of the shortest string.
Overall, the time complexity is O(n log n + m).
# Space Complexity:

The space complexity is O(1) if we do not consider the space used by the input array and the sort operation. The sort operation typically requires O(n) space, but this is dependent on the sorting algorithm used by the language's standard library.

# Remove Duplicates from Sorted Array

## Problem Description
Given a sorted integer array `nums`, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

### Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

### Example 1
**Input:**
```python
nums = [1, 1, 2]
```
## Approach
We use a two-pointer technique to solve this problem efficiently:

## Initialization:

Use two pointers: i to iterate through the array and j to track the position of the next unique element.
Iterate through the array:

If the current element nums[i] is not equal to the previous element nums[i - 1], then it's a unique element.
Place this unique element at position nums[j] and increment j.
Return:

The pointer j will be the count of unique elements, indicating the number of unique elements in the modified array.
## Complexity Analysis
Time Complexity: O(n), where n is the length of the array nums. We only iterate through the array once.
Space Complexity: O(1). We use a constant amount of extra space for the two pointers.

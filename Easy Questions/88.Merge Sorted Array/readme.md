# Merge Sorted Arrays

## Introduction

This project provides a solution to the problem of merging two sorted integer arrays `nums1` and `nums2` into a single sorted array. The solution ensures that the final sorted array is stored in-place within `nums1`. The length of `nums1` is `m + n`, where the first `m` elements denote the initial elements to be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.

## Problem Statement

Given two integer arrays `nums1` and `nums2` sorted in non-decreasing order, and two integers `m` and `n` representing the number of elements in `nums1` and `nums2` respectively, merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function but instead be stored inside the array `nums1`.

## Approach

1. **Initialize Pointers**:
   - `p1` to point to the last initialized element of `nums1` (`m - 1`).
   - `p2` to point to the last element of `nums2` (`n - 1`).
   - `p` to point to the last position in `nums1` (`m + n - 1`).

2. **Merge Arrays from the End**:
   - Compare the elements pointed to by `p1` and `p2`.
   - Place the larger element at position `p` in `nums1` and move the respective pointer (`p1` or `p2`) and `p`.

3. **Copy Remaining Elements**:
   - If any elements are left in `nums2`, copy them into `nums1` starting from the back.

4. **Edge Cases**:
   - If `nums2` is empty, `nums1` remains unchanged.
   - If `nums1` is empty (excluding the placeholders), all elements from `nums2` are copied into `nums1`.

## Code Snippet

```python
def merge(nums1, m, nums2, n):
    """
    Merge nums2 into nums1 as one sorted array.

    Parameters:
    nums1 (List[int]): The first sorted array with extra space for nums2.
    m (int): The number of initialized elements in nums1.
    nums2 (List[int]): The second sorted array.
    n (int): The number of elements in nums2.

    Returns:
    None: The merged array is stored in nums1.
    """
    p1, p2 = m - 1, n - 1
    p = m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# Example
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
```
## Explanation
Pointers Initialization: p1 points to the last initialized element of nums1, p2 points to the last element of nums2, and p points to the last position in nums1 where the merged elements will be placed.
Merging from the End: By comparing elements from the end of both arrays and placing the larger element at the end of nums1, we avoid overwriting elements that haven't been processed yet.
Copy Remaining Elements: After the main loop, if there are any elements left in nums2, they are copied into nums1.
Complexities
## Time Complexity
The time complexity is O(m+n), as we process each element from both arrays exactly once.
Space Complexity
## The space complexity is O(1), as we are merging the arrays in-place without using any additional space.

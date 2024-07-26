# Two Sum Problem Solution

## Approach

To solve the Two Sum problem efficiently, we use a hash map (dictionary) to track the indices of the numbers we have encountered so far. This approach allows us to find the pair of indices in a single pass through the array.

### Steps:

1. **Initialize a Hash Map**: Create a dictionary to store each number and its index as we iterate through the array.

2. **Iterate Through the Array**:
   - For each number, calculate its complement by subtracting the number from the target.
   - Check if this complement is already in the hash map.
   - If found, return the indices of the complement and the current number.
   - If not found, add the current number and its index to the hash map.

### Reasoning

- **Efficiency**: Using a hash map allows us to achieve an average time complexity of \(O(n)\), where \(n\) is the number of elements in the array. This is because both insertion and lookup operations in a hash map are average \(O(1)\).
- **Single Pass**: We only need to make one pass through the array, making this approach both time-efficient and space-efficient compared to a brute force solution.

## Complexity Comparison

### Brute Force Approach

- **Time Complexity**: \(O(n^2)\)
  - This approach involves checking all possible pairs of numbers to find the pair that sums up to the target. With \(n\) numbers, this results in \(O(n^2)\) operations.

- **Space Complexity**: \(O(1)\)
  - No additional space is required beyond the input array.

### Hash Map Approach

- **Time Complexity**: \(O(n)\)
  - The hash map allows us to find the complement of the current number in constant time. As we iterate through the array once, the overall time complexity is \(O(n)\).

- **Space Complexity**: \(O(n)\)
  - We use additional space for the hash map to store the indices of the numbers encountered.

## Example

For `nums = [2, 7, 11, 15]` and `target = 9`:
- Iterate through the array:
  - For `2`, complement is `7`. Not in hash map.
  - For `7`, complement is `2`. Found in hash map at index `0`.
  - Return indices `[0, 1]`.

This method ensures we efficiently find the indices with minimal computation and is optimal for large inputs.


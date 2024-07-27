# Plus One Function

## Approach

1. **Convert Digits to Integer**:
   - Initialize `sum` to zero. Iterate through the list `digits` and convert it to a single integer by iterating through each digit and constructing the number.

2. **Increment the Integer**:
   - Add `1` to the integer value obtained in the previous step.

3. **Convert Integer Back to List of Digits**:
   - Use a loop to extract each digit from the incremented integer and store it in the `result` list.
   - Reverse the `result` list to get the final list of digits in the correct order.

4. **Return the Result**:
   - Return the reversed `result` list.

## Complexities

### Time Complexity
- The time complexity is \(O(n)\), where \(n\) is the number of digits in the input list. This is due to converting the list to an integer, incrementing it, and converting it back to a list.

### Space Complexity
- The space complexity is \(O(n)\) as well, where \(n\) is the number of digits in the input list. This is due to storing the digits in the `result` list.

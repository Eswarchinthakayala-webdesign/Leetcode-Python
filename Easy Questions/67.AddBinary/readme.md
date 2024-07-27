# Add Binary Function

## Approach

1. **Convert Binary to Decimal**:
   - Convert the binary strings `a` and `b` to decimal integers using Python's `int()` function with base 2.

2. **Add the Two Decimal Integers**:
   - Add the two decimal integers obtained from the previous step.

3. **Convert the Sum Back to Binary**:
   - Convert the resulting sum back to a binary string using Python's `bin()` function.
   - Remove the '0b' prefix from the binary string by slicing the string with `[2:]`.

4. **Return the Result**:
   - Return the binary string representation of the sum.
## Time Complexity
The time complexity is O(max(m,n)), where m,n are the lengths of the input binary strings a and b, respectively. This is due to the conversion operations and the addition of two integers.
## Space Complexity
The space complexity isO(max(m,n)), as the resulting binary string has a length proportional to the maximum length of the input binary strings.

## Integer Digit Reversal
 Problem Description
 The task is to reverse the digits of a signed 32-bit integer x. If reversing x causes the value to fall outside the range of a 32-bit signed integer (from -2^31 to 2^31 - 1), the function should return 0
### Approach
# Identify the Sign:

Determine whether x is positive or negative. Use this to restore the sign of the reversed number.
Convert x to its absolute value for simplicity in processing.
## Reverse the Digits:

Initialize reversed_num to 0. This variable will store the reversed number.
Use a loop to extract digits from x:
Extract the last digit using x % 10.
Remove the last digit from x using integer division (x //= 10).
Before updating reversed_num, check for potential overflow by comparing with maximum allowed values.
Handle Overflow:

Ensure the reversed number does not exceed the 32-bit signed integer limits:
Positive Overflow Check: If adding the next digit would cause reversed_num to exceed 2,147,483,647.
Negative Overflow Check: If the reversed number becomes less than -2,147,483,648.
Restore the Sign:

Multiply reversed_num by the original sign to get the final result.
## Overflow Explanation
Overflow occurs when a calculation exceeds the limits of the data type used to store the result. In this case, for a 32-bit signed integer:

Maximum Value (INT_MAX): 2,147,483,647
Minimum Value (INT_MIN): -2,147,483,648
When reversing the digits of a number, if the resultant value exceeds these limits, overflow happens.

## Why Overflow Happens:

# Arithmetic Operations:

When reversing, each new digit is appended to the growing reversed_num. If this number grows too large, it can exceed the maximum allowed value for a 32-bit signed integer.
Overflow Check:

The condition reversed_num > (max - r) // 10 checks whether adding the next digit (r) would exceed INT_MAX.
If this condition is true, adding another digit would cause overflow, so the function returns 0.
Complexity Analysis
## Time Complexity:

Loop Iterations: The while x != 0 loop runs for each digit in x.
Number of Digits: For a 32-bit signed integer, the maximum number of digits is 10.
Operations per Iteration: Each iteration involves constant-time operations (modulus, integer division, comparison, and multiplication).
Time Complexity: O(d), where d is the number of digits in x. For a 32-bit integer, this is effectively O(1) since d is bounded by a constant.
## Space Complexity:

Auxiliary Space: Uses a fixed amount of space for variables (max, min, sign, reversed_num, and r).
No Extra Data Structures: No additional data structures grow with input size.
Space Complexity: O(1), as the space used does not depend on the size of the input.

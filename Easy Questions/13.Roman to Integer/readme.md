## Roman Numeral to Integer Converter
# Problem
Roman numerals are a numeral system originating from ancient Rome, used throughout the Roman Empire. They are based on certain symbols and rules for combining these symbols to represent numbers. The Roman numeral system uses seven symbols: I, V, X, L, C, D, and M.

The task is to convert a Roman numeral string into its corresponding integer value. For instance, the Roman numeral "III" should be converted to the integer 3, and "MCMXCIV" should be converted to the integer 1994.

## Problem Approach
To solve this problem, we need to follow these steps:

Define Roman Values: Create a mapping of Roman numeral characters to their integer values.

Iterate Through the Roman Numeral String:

Traverse each character of the Roman numeral string.
For each character, determine its integer value.
Use a rule to handle cases where subtraction is involved (e.g., "IV" for 4).
Handle Subtraction Cases:

If the value of the current numeral is greater than the previous numeral, this indicates a subtraction case. We need to adjust the total accordingly by subtracting twice the previous value (since it was added once in the previous step).
Calculate the Total:

Sum up the values of the numerals, applying the subtraction rule where necessary.
Return the Final Integer Value.

# Example
Input: "MCMXCIV"
Output: 1994
Explanation:

M (1000)
CM (900)
XC (90)
IV (4)
Total = 1000 + 900 + 90 + 4 = 1994
## Complexity Analysis
# Time Complexity
O(n): The time complexity is O(n), where n is the length of the Roman numeral string. This is because we traverse the string once, performing constant-time operations for each character.
# Space Complexity
O(1): The space complexity is O(1) because we are only using a fixed amount of extra space for variables (total, prev_value, value) regardless of the input size.

# My Sqrt Function

## Approach

1. **Calculate the Square Root**:
   - Use Python's `math.sqrt()` function to calculate the square root of the input number `x`.

2. **Convert to Integer**:
   - Convert the result to an integer using Python's `int()` function. This will truncate the decimal part, giving the integer part of the square root.

3. **Return the Result**:
   - Return the integer part of the square root.

## Code Snippet

```python
from math import sqrt

def mysqrt(x):
    """
    Calculate the integer part of the square root of a given number.

    Parameters:
    x (int): The input number.

    Returns:
    int: The integer part of the square root of x.
    """
    return int(sqrt(x))
```
# Complexities
Time Complexity
The time complexity is O(1) because the calculation of the square root using math.sqrt() is a constant time operation.
# Space Complexity
The space complexity is O(1) as the function uses a constant amount of additional space regardless of the input size.
# Explanation
Square Root Calculation: sqrt(x) computes the square root of x.
Conversion to Integer: int() truncates the decimal part of the result, providing the integer part of the square root.
